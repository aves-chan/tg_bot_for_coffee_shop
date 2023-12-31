from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from sql_queries.db_client import DB_client

from keyboard.keyboard_client import KB_client

client_registration_router = Router()

kb_client = KB_client()

db_client = DB_client()

@client_registration_router.message(F.contact.user_id == F.from_user.id)
async def handler_phone_number(msg: types.Message):
    db_client.add_new_user(telegram_id=msg.from_user.id,
                           firstname=msg.from_user.first_name,
                           username=msg.from_user.username,
                           phone_number=msg.contact.phone_number)
    await msg.answer(text="Успешно!", reply_markup=ReplyKeyboardRemove())
    await msg.answer(text="Добро пожаловать!", reply_markup=kb_client.start_client())