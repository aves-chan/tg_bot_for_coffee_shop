from aiogram import Router, types, F
from aiogram.enums import ParseMode
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from sql_queries.sql_client import db_add_new_user
from state.state_client import Client_state
from keyboard.keyboard_client import *

client_router = Router()


@client_router.message(F.contact.user_id == F.from_user.id)
async def handler_phone_number(msg: types.Message):
    db_add_new_user(telegram_id=msg.from_user.id,
                    firstname=msg.from_user.first_name,
                    username=msg.from_user.username,
                    phone_number=msg.contact.phone_number)
    await msg.answer(reply_markup=ReplyKeyboardRemove)
    await msg.answer(text="Отлично!", reply_markup=kb_start_client())




@client_router.callback_query(StateFilter(Client_state.start_order_state), F.data == "Заказать")
async def handler_order_user(cd: types.CallbackQuery, state: FSMContext):
    await cd.message.delete()
    await cd.message.answer(text="<b>Выбери категорию</b>", parse_mode=ParseMode.HTML, reply_markup=kb_order_main_menu())
    await cd.answer()
@client_router.callback_query(StateFilter(Client_state.drinks_order_state), F.data == "Назад к главному меню")
async def handler_on_cancel_order_user(cd: types.CallbackQuery, state: FSMContext):
    await cd.message.delete()
    await cd.message.answer(text="<b>Выбери категорию</b>", parse_mode=ParseMode.HTML, reply_markup=kb_order_main_menu())
    await cd.answer()

@client_router.callback_query(StateFilter(Client_state.start_order_state))
async def handler_main_categories_user(cd: types.CallbackQuery, state: FSMContext):
    await cd.message.delete()
    if cd.data == "Напитки":
        await cd.message.answer(text="Напитки", reply_markup=kb_order_drinks_menu())
        await state.set_state(state=Client_state.drinks_order_state)
    elif cd.data == "Еда":
        await cd.message.answer(text="<b>ПОКА В РАЗРАБОТКЕ</b>", parse_mode=ParseMode.HTML, reply_markup=kb_order_main_menu())
    elif cd.data == "Десерты":
        await cd.message.answer(text="<b>ПОКА В РАЗРАБОТКЕ</b>", parse_mode=ParseMode.HTML, reply_markup=kb_order_main_menu())
    elif cd.data == "Корзина":
        await cd.message.answer(text="Корзина", parse_mode=ParseMode.HTML)
    await cd.answer()

@client_router.callback_query(StateFilter(Client_state.drinks_order_state))
async def handler_category_drinks(cd: types.CallbackQuery, state: FSMContext):
    if cd.data == "Кофе":
        await cd.message.delete()
        await cd.message.answer(text="Какое кофе хотите добавить в корзину?", reply_markup=kb_order_drinks_coffee())
        await state.set_state(Client_state.coffee_order_state)
        await cd.answer()
    elif cd.data == "Чай":
        await cd.message.delete()
        await cd.message.answer(text="Какой чай хотите добавить в корзину?", reply_markup=kb_order_drinks_tea())
        await state.set_state(Client_state.tea_order_state)
        await cd.answer()

@client_router.callback_query(StateFilter(Client_state.coffee_order_state))
async def handler_category_drinks(cd: types.CallbackQuery, state: FSMContext):
    await cd.message.delete()
    await cd.message.answer(text="ПОКА В РАЗРАБОТКЕ", reply_markup=kb_order_main_menu())
    await state.set_state(Client_state.start_order_state)
    await cd.answer()

@client_router.callback_query(StateFilter(Client_state.tea_order_state))
async def handler_category_drinks(cd: types.CallbackQuery, state: FSMContext):
    await cd.message.delete()
    await cd.message.answer(text="ПОКА В РАЗРАБОТКЕ", reply_markup=kb_order_main_menu())
    await state.set_state(Client_state.start_order_state)
    await cd.answer()