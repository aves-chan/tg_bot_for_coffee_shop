from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram import Router, types, F
from aiogram.enums import ParseMode


from sql_queries.sql_client import *
from state.state_client import Client_state
from keyboard.keyboard_client import *

client_drinks_quantity_selection_router = Router()

@client_drinks_quantity_selection_router.callback_query(StateFilter(Client_state.coffee_order_state), F.data.regexp(r'page\d+'))
async def handler_category_coffee_next_or_previous_pages(cd: types.CallbackQuery, state: FSMContext):
    data = cd.data
    page = int(data[4::])
    if len(db_select_products_for_generate_keyboard(products="Кофе", offset=page)) == 0:
        await cd.message.delete()
        await cd.message.answer(text="НЕТУ БОЛЬШЕ")
        await cd.answer()
    else:
        kb_drinks = kb_add_in_cart_all_products(array_products=db_select_products_for_generate_keyboard(products="Кофе", offset=page),
                                                page_number=page // 6,
                                                page_number_next=page + 6)
        await cd.message.delete()
        await cd.message.answer(text="Какое кофе хотите добавить в корзину?", reply_markup=kb_drinks)
        await cd.answer()


@client_drinks_quantity_selection_router.callback_query(StateFilter(Client_state.coffee_order_state))
async def handler_category_coffee(cd: types.CallbackQuery, state: FSMContext):
    if cd.data == "Назад к выбору категорий":
        await cd.message.delete()
        await cd.message.answer(text="Напитки", reply_markup=kb_order_drinks_category())
        await state.set_state(state=Client_state.drinks_order_state)
        await cd.answer()
    else:
        coffee = db_select_one_product(cd.data)
        if coffee[2] == None:
            await cd.message.delete()
            await cd.message.answer(text=f"""<b>{coffee[1]}</b>
<b>Описание:</b> {coffee[3]}
    
<b>Цена:</b> {coffee[4]}""", parse_mode=ParseMode.HTML, reply_markup=kb_adding_to_cart_drinks(1))
            await state.set_state(Client_state.coffee_adding_to_cart)
            await cd.answer()
        else:
            await cd.message.delete()
            await cd.message.answer_photo(photo=coffee[2], caption=f"""<b>{coffee[1]}</b>
<b>Описание:</b> {coffee[3]}
    
<b>Цена:</b> {coffee[4]}""", parse_mode=ParseMode.HTML, reply_markup=kb_adding_to_cart_drinks(1))
            await state.set_state(Client_state.coffee_adding_to_cart)
            await cd.answer()

@client_drinks_quantity_selection_router.callback_query(StateFilter(Client_state.tea_order_state), F.data.regexp(r'page\d+'))
async def handler_category_tea_next_or_previous_pages(cd: types.CallbackQuery, state: FSMContext):
    data = cd.data
    page = int(data[4::])
    if len(db_select_products_for_generate_keyboard(products="Кофе", offset=page)) == 0:
        await cd.message.delete()
        await cd.message.answer(text="НЕТУ БОЛЬШЕ")
        await cd.answer()
    else:
        kb_drinks = kb_add_in_cart_all_products(
            array_products=db_select_products_for_generate_keyboard(products="Чай", offset=page),
            page_number=page // 6,
            page_number_next=page + 6)
        await cd.message.delete()
        await cd.message.answer(text="Какое чай хотите добавить в корзину?", reply_markup=kb_drinks)
        await cd.answer()

@client_drinks_quantity_selection_router.callback_query(StateFilter(Client_state.tea_order_state))
async def handler_category_tea(cd: types.CallbackQuery, state: FSMContext):
    if cd.data == "Назад к выбору напитков":
        await cd.message.delete()
        await cd.message.answer(text="Напитки", reply_markup=kb_order_drinks_category())
        await state.set_state(state=Client_state.drinks_order_state)
        await cd.answer()
    else:
        tea = db_select_one_product(cd.data)
        if tea[2] == None:
            await cd.message.delete()
            await cd.message.answer(text=f"""<b>{tea[1]}</b>
<b>Описание:</b> {tea[3]}

<b>Цена:</b> {tea[4]}""", parse_mode=ParseMode.HTML, reply_markup=kb_adding_to_cart_drinks(1))
            await cd.answer()
            await state.set_state(Client_state.tea_adding_to_cart)
        else:
            await cd.message.delete()
            await cd.message.answer_photo(photo=tea[2], caption=f"""<b>{tea[1]}</b>
<b>Описание:</b> {tea[3]}

<b>Цена:</b> {tea[4]}""", parse_mode=ParseMode.HTML, reply_markup=kb_adding_to_cart_drinks(1))
            await state.set_state(Client_state.tea_adding_to_cart)
            await cd.answer()