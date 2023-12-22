from aiogram import Router, types, F
from aiogram.types import ReplyKeyboardRemove

from sql_queries.sql_client import db_add_new_user

from keyboard.keyboard_client import *


client_registration_router = Router()


@client_registration_router.message(F.contact.user_id == F.from_user.id)
async def handler_phone_number(msg: types.Message):
    db_add_new_user(telegram_id=msg.from_user.id,
                    firstname=msg.from_user.first_name,
                    username=msg.from_user.username,
                    phone_number=msg.contact.phone_number)
    await msg.answer(reply_markup=ReplyKeyboardRemove)
    await msg.answer(text="Отлично!", reply_markup=kb_start_client())