import asyncio
import logging
import psycopg2
from aiogram.enums import ParseMode
from aiohttp import web

import config
from fastapi import FastAPI

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

from config_gitignore import WEB_SERVER_HOST_GITIGNORE, WEB_SERVER_PORT_GITIGNORE, WEBHOOK_PATH_GITIGNORE, \
    WEBHOOK_SECRET_GITIGNORE, BASE_WEBHOOK_URL_GITIGNORE
from keyboard.keyboard_client import kb_start_client, kb_phone_number
from handlers.handlers_client.handlers_client_order import client_order_router
from state.state_client import Client_state

dp = Dispatcher()

app = FastAPI()

WEB_SERVER_HOST = WEB_SERVER_HOST_GITIGNORE
# Port for incoming request from reverse proxy. Should be any available port
WEB_SERVER_PORT = WEB_SERVER_PORT_GITIGNORE

# Path to webhook route, on which Telegram will send requests
WEBHOOK_PATH = WEBHOOK_PATH_GITIGNORE
# Secret key to validate requests from Telegram (optional)
WEBHOOK_SECRET = WEBHOOK_SECRET_GITIGNORE
# Base URL for webhook will be used to generate webhook URL for Telegram,
# in this example it is used public DNS with HTTPS support
BASE_WEBHOOK_URL = BASE_WEBHOOK_URL_GITIGNORE

async def on_startup(bot: Bot) -> None:
    # If you have a self-signed SSL certificate, then you will need to send a public
    # certificate to Telegram
    await bot.set_webhook(f"{BASE_WEBHOOK_URL}{WEBHOOK_PATH}", secret_token=WEBHOOK_SECRET)

def chek_user(id_telegram: int):
    conn = psycopg2.connect(dbname="coffee_shop", user="vsevolod", password=config.PASSWORD_POSTGRESQL, host=config.IP_MY_SERVER, port="5432")
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



dp.include_routers(client_order_router)


def main() -> None:
    dp.startup.register(on_startup)
    bot = Bot(config.TOKEN, parse_mode=ParseMode.HTML)
    app = web.Application()
    webhook_requests_handler = SimpleRequestHandler(dispatcher=dp, bot=bot, secret_token=WEBHOOK_SECRET)
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)
    setup_application(app, dp, bot=bot)
    web.run_app(app, host=WEB_SERVER_HOST, port=WEB_SERVER_PORT)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())


