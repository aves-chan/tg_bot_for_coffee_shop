from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from sql_queries.sql_client import db_add_new_user

from keyboard.keyboard_client import *
from state.state_client import Client_state

client_registration_router = Router()


@client_registration_router.message(F.contact.user_id == F.from_user.id)
async def handler_phone_number(msg: types.Message, state: FSMContext):
    db_add_new_user(telegram_id=msg.from_user.id,
                    firstname=msg.from_user.first_name,
                    username=msg.from_user.username,
                    phone_number=msg.contact.phone_number)
    await msg.answer(text="Успешно!", reply_markup=ReplyKeyboardRemove())
    await msg.answer(text="Добро пожаловать!", reply_markup=kb_start_client())
    await state.set_state(Client_state.start_order_state)