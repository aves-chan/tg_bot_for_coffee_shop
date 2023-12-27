from aiogram import Router, types, F
from aiogram.enums import ParseMode
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext

from handlers.handlers_client.handlers_desserts_quantity_selection import client_desserts_quantity_selection_router
from handlers.handlers_client.handlers_drinks_quantity_selection import client_drinks_quantity_selection_router
from handlers.handlers_client.handlers_meal_quantity_selection import client_meal_quantity_selection_router
from handlers.handlers_client.handlers_registration_client import client_registration_router
from sql_queries import sql_client
from sql_queries.sql_client import *
from state.state_client import Client_state
from keyboard.keyboard_client import *

client_order_router = Router()
client_order_router.include_routers(client_registration_router, client_drinks_quantity_selection_router, client_meal_quantity_selection_router, client_desserts_quantity_selection_router)


@client_order_router.callback_query(StateFilter(Client_state.start_order_state), F.data == "Заказать")
async def handler_order_user(cd: types.CallbackQuery, state: FSMContext):
    await cd.message.delete()
    await cd.message.answer(text="<b>Выбери категорию</b>", parse_mode=ParseMode.HTML, reply_markup=kb_order_main_menu())
    await cd.answer()

@client_order_router.callback_query(StateFilter(Client_state.start_order_state))
async def handler_main_categories_user(cd: types.CallbackQuery, state: FSMContext):
    await cd.message.delete()
    if cd.data == "Напитки":
        await cd.message.answer(text="Напитки", reply_markup=kb_order_drinks_category())
        await state.set_state(state=Client_state.drinks_order_state)
    elif cd.data == "Еда":
        await cd.message.answer(text="Еда", reply_markup=kb_order_meal_category())
        await state.set_state(state=Client_state.meal_order_state)
    elif cd.data == "Десерты":
        await cd.message.answer(text="<b>ПОКА В РАЗРАБОТКЕ</b>", parse_mode=ParseMode.HTML, reply_markup=kb_order_main_menu())
    elif cd.data == "Корзина":
        await cd.message.answer(text="Корзина", parse_mode=ParseMode.HTML)
    await cd.answer()

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
            kb_drinks = kb_add_in_cart_all_products(db_select_all_products("Кофе"), page_number=0)
            await cd.message.delete()
            await cd.message.answer(text="Какое кофе хотите добавить в корзину?", reply_markup=kb_drinks)
            await state.set_state(Client_state.coffee_order_state)
            await cd.answer()
        elif cd.data == "Чай":
            kb_drinks = kb_add_in_cart_all_products(db_select_all_products("Чай"), page_number=0)
            await cd.message.delete()
            await cd.message.answer(text="Какой чай хотите добавить в корзину?", reply_markup=kb_drinks)
            await state.set_state(Client_state.tea_order_state)
            await cd.answer()


@client_order_router.callback_query(StateFilter(Client_state.meal_order_state), F.data != "Назад к главному меню")
async def handler_category_meal(cd: types.CallbackQuery, state: FSMContext):
    if cd.data == "Завтраки":
        if db_select_all_products("Завтраки") == None:
            await cd.message.delete()
            await cd.message.answer(text="Закончилось все из этой категории(", reply_markup=kb_order_meal_category())
            await cd.answer()
        else:
            kb_breakfasts = kb_add_in_cart_all_products(db_select_all_products("Завтрак"), page_number=0)
            await cd.message.delete()
            await cd.message.answer(text="Завтраки", reply_markup=kb_breakfasts)
            await state.set_state(Client_state.breakfasts_quantity_selection_state)
            await cd.answer()
    elif cd.data == "Сэндвичи":
        if db_select_all_products("Сэндвич") == None:
            await cd.message.delete()
            await cd.message.answer(text="Закончилось все из этой категории(", reply_markup=kb_order_meal_category())
            await cd.answer()
        else:
            kb_sandwich = kb_add_in_cart_all_products(db_select_all_products("Сэндвич"), page_number=0)
            await cd.message.delete()
            await cd.message.answer(text="Сэндвичи", reply_markup=kb_sandwich)
            await state.set_state(Client_state.sandwich_quantity_selection_state)
            await cd.answer()

