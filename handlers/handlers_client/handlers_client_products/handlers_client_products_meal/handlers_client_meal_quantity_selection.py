from aiogram import Router, types, F
from aiogram.enums import ParseMode
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.methods import *

from sql_queries import sql_client
from sql_queries.sql_client import *
from state.state_client import Client_state
from keyboard.keyboard_client import *

client_meal_quantity_selection_router = Router()


@client_meal_quantity_selection_router.callback_query(StateFilter(Client_state.breakfasts_quantity_selection_state))
async def handler_breakfasts_quantity_selection(cd: types.CallbackQuery, state: FSMContext):
    breakfast = db_select_one_product(cd.data)
    if breakfast[2] == None:
        await cd.message.delete()
        await cd.message.answer(text=f"""<b>{breakfast[1]}</b>
<b>Описание:</b> {breakfast[2]}

<b>Цена:</b> {breakfast[3]}""", parse_mode=ParseMode.HTML, reply_markup=kb_adding_to_cart_meal_or_dessert(breakfast))
        await state.set_state(Client_state.breakfasts_quantity_selection2_state)
        await cd.answer()
    else:
        await cd.message.delete()
        await cd.message.answer_photo(photo=breakfast[2], caption=f"""<b>{breakfast[1]}</b>
<b>Описание:</b> {breakfast[2]}

<b>Цена:</b> {breakfast[3]}""", parse_mode=ParseMode.HTML, reply_markup=kb_adding_to_cart_meal_or_dessert(breakfast))
        await state.set_state(Client_state.breakfasts_quantity_selection2_state)
        await cd.answer()


@client_meal_quantity_selection_router.callback_query(StateFilter(Client_state.sandwich_quantity_selection_state))
async def handler_sandwich_quantity_selection(cd: types.CallbackQuery, state: FSMContext):
    sandwich = db_select_one_product(cd.data)
    if sandwich[2] == None:
        await cd.message.delete()
        await cd.message.answer(text=f"""<b>{sandwich[1]}</b>
<b>Описание:</b> {sandwich[3]}

<b>Цена:</b> {sandwich[4]}""", parse_mode=ParseMode.HTML, reply_markup=kb_adding_to_cart_meal_or_dessert(sandwich))
        await state.set_state(Client_state.sandwich_quantity_selection2_state)
        await cd.answer()
    else:
        await cd.message.delete()
        await cd.message.answer_photo(photo=sandwich[2], caption=f"""<b>{sandwich[1]}</b>
<b>Описание:</b> {sandwich[2]}

<b>Цена:</b> {sandwich[3]}""", parse_mode=ParseMode.HTML, reply_markup=kb_adding_to_cart_meal_or_dessert(sandwich))
        await state.set_state(Client_state.sandwich_quantity_selection2_state)
        await cd.answer()
