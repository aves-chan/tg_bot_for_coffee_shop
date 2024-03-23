import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message

from aiogram_dialog import (DialogManager, setup_dialogs, StartMode)

from client.dialog.client_main_menu import dialog_main
from client.client_state import Client_main_state, Client_new_user_state
from client.dialog.client_new_user import dialog_new_user
from client.dialog.client_product_menu import dialog_product_menu
from client.dialog.client_profile_menu import dialog_profile
from config import TOKEN
from database_queries import db_queries

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)

storage = MemoryStorage()
dp = Dispatcher(storage=storage)

dp.include_routers(dialog_main, dialog_profile, dialog_new_user, dialog_product_menu)
setup_dialogs(dp)


@dp.message(Command("start"))
async def start(message: Message, dialog_manager: DialogManager):
    user = db_queries.check_user(telegram_id=message.from_user.id)
    if user == None:
        await dialog_manager.start(Client_new_user_state.phone_number, mode=StartMode.RESET_STACK)
    else:
        await dialog_manager.start(Client_main_state.main_menu, mode=StartMode.RESET_STACK)


if __name__ == '__main__':
    dp.run_polling(bot, skip_updates=True)
