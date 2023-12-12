import asyncio
import logging
import psycopg2
import config

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


from keyboard.keyboard_client import kb_start_client, kb_phone_number
from handlers import handlers_client, handlers_worker, handlers_owner
from state.state_client import Client_state

dp = Dispatcher()

def chek_user(id_telegram: int):
    conn = psycopg2.connect(dbname="db_users", user="vsevolod", password=config.PASSWORD_POSTGRESQL, host=config.IP_MY_SERVER, port="5432")
    cursor = conn.cursor()
    cursor.execute(f"SELECT tag FROM users WHERE telegram_id = {id_telegram}")
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

@dp.message(Command("start"))
async def start(msg: types.Message, state: FSMContext):
    db_user = chek_user(msg.from_user.id)
    if db_user == None:
        await msg.answer(text="Привет! Перед тем как заказать еду нужен твой номер телефона)",reply_markup=kb_phone_number())
    elif db_user[0] == "Гость":
        await msg.answer(text=f"Привет", reply_markup=kb_start_client())
        await state.set_state(Client_state.start_order_state)
    elif db_user[0] == "Сотрудник":
        await msg.answer("Привет сотрудник")
    elif db_user[0] == "Владелец":
        await msg.answer("Привет владелец")



dp.include_routers(handlers_client.client_router)


async def main():
    bot = Bot(token=config.TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())


