import asyncio
import logging
import typing

import psycopg2
from aiogram.enums import ParseMode

import config
from fastapi import FastAPI

from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters import Command

from handlers.handlers_client.handlers_client_creating_shopping_cart.handlers_client_product_cart import \
    client_product_cart_router
from handlers.handlers_client.handlers_client_creating_shopping_cart.handlers_client_product_menu import \
    client_product_menu_router
from handlers.handlers_client.handlers_client_for_adding_user_to_database.handlers_registration_user import \
    client_registration_router
from keyboard.keyboard_client import KB_client

dp = Dispatcher()

app = FastAPI()

kb_client = KB_client()


def chek_user(id_telegram: int) -> typing.Tuple:
    conn = psycopg2.connect(dbname="coffee_shop", user="vsevolod", password=config.PASSWORD_POSTGRESQL, host=config.IP_MY_SERVER, port="5432")
    cursor = conn.cursor()
    cursor.execute(f"SELECT tag FROM users WHERE telegram_id = {id_telegram}")
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

@dp.message(Command("start"))
async def handler_start(msg: types.Message):
    db_user = chek_user(msg.from_user.id)
    if db_user == None:
        await msg.answer(text="Привет! Перед тем как заказать еду нужен твой номер телефона)", reply_markup=kb_client.phone_number())
    elif db_user[0] == "Гость":
        await msg.answer(text=f"Главное меню", reply_markup=kb_client.main_menu())
    elif db_user[0] == "Сотрудник":
        await msg.answer("Привет сотрудник")
    elif db_user[0] == "Владелец":
        await msg.answer("Привет владелец")
@dp.callback_query(F.data == "Назад к главному меню")
async def handler_client_back_main_button(cd: types.CallbackQuery):
    await cd.message.edit_text(text="Главное меню", reply_markup=kb_client.main_menu())
    await cd.answer()

client_main_router = Router()
client_main_router.include_routers(client_registration_router, client_product_menu_router, client_product_cart_router)

dp.include_routers(client_main_router)

async def main() -> None:
    bot = Bot(config.TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())


