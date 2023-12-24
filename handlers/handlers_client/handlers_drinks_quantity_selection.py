from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram import Router, types, F
from aiogram.enums import ParseMode

from sql_queries.sql_client import db_select_all_drinks, db_select_one_drink
from state.state_client import Client_state
from keyboard.keyboard_client import *

client_drinks_quantity_selection_router = Router()

@client_drinks_quantity_selection_router.callback_query(StateFilter(Client_state.drinks_order_state))
async def handler_category_drinks(cd: types.CallbackQuery, state: FSMContext):
    if cd.data == "Назад к главному меню":
        await cd.message.delete()
        await cd.message.answer(text="<b>Выбери категорию</b>", parse_mode=ParseMode.HTML,
                                reply_markup=kb_order_main_menu())
        await state.set_state(Client_state.start_order_state)
        await cd.answer()
    else:
        if cd.data == "Кофе":
            kb_drinks = kb_add_in_cart_drinks(db_select_all_drinks("Кофе"), page_number=0)
            await cd.message.delete()
            await cd.message.answer(text="Какое кофе хотите добавить в корзину?", reply_markup=kb_drinks)
            await state.set_state(Client_state.coffee_order_state)
            await cd.answer()
        elif cd.data == "Чай":
            kb_drinks = kb_add_in_cart_drinks(db_select_all_drinks("Чай"), page_number=0)
            await cd.message.delete()
            await cd.message.answer(text="Какой чай хотите добавить в корзину?", reply_markup=kb_drinks)
            await state.set_state(Client_state.tea_order_state)
            await cd.answer()

@client_drinks_quantity_selection_router.callback_query(StateFilter(Client_state.coffee_order_state))
async def handler_category_coffee(cd: types.CallbackQuery, state: FSMContext):
    if cd.data == "Назад к выбору напитков":
        await cd.message.delete()
        await cd.message.answer(text="Напитки", reply_markup=kb_order_drinks_category())
        await state.set_state(state=Client_state.drinks_order_state)
        await cd.answer()
    else:
        coffee = db_select_one_drink(cd.data)
        if coffee[2] == None:
            await cd.message.delete()
            await cd.message.answer(text=f"""<b>{coffee[1]}</b>
        <b>Описание:</b> {coffee[2]}
    
        <b>Цена:</b> {coffee[3]}""", parse_mode=ParseMode.HTML, reply_markup=kb_adding_to_cart_any_products(coffee))
            await cd.answer()
        else:
            await cd.message.delete()
            await cd.message.answer_photo(photo=coffee[2], caption=f"""<b>{coffee[1]}</b>
        <b>Описание:</b> {coffee[2]}
    
        <b>Цена:</b> {coffee[3]}""", parse_mode=ParseMode.HTML, reply_markup=kb_adding_to_cart_any_products(coffee))
            await cd.answer()

@client_drinks_quantity_selection_router.callback_query(StateFilter(Client_state.tea_order_state))
async def handler_category_tea(cd: types.CallbackQuery, state: FSMContext):
    if cd.data == "Назад к выбору напитков":
        await cd.message.delete()
        await cd.message.answer(text="Напитки", reply_markup=kb_order_drinks_category())
        await state.set_state(state=Client_state.drinks_order_state)
        await cd.answer()
    else:
        tea = db_select_one_drink(cd.data)
        if tea[2] == None:
            await cd.message.delete()
            await cd.message.answer(text=f"""<b>{tea[1]}</b>
        <b>Описание:</b> {tea[2]}

        <b>Цена:</b> {tea[3]}""", parse_mode=ParseMode.HTML, reply_markup=kb_adding_to_cart_any_products(tea))
            await cd.answer()
        else:
            await cd.message.delete()
            await cd.message.answer_photo(photo=tea[2], caption=f"""<b>{tea[1]}</b>
        <b>Описание:</b> {tea[2]}

        <b>Цена:</b> {tea[3]}""", parse_mode=ParseMode.HTML, reply_markup=kb_adding_to_cart_any_products(tea))
            await cd.answer()