import json

from aiogram import Router, types, F
from aiogram.enums import ParseMode

from sql_queries.db_client import DB_client
from keyboard.keyboard_client import KB_client

client_product_cart_router = Router()

kb_client = KB_client()

db_client = DB_client()

@client_product_cart_router.callback_query(F.data == "Моя корзина")
async def handler_client_cart(cd: types.CallbackQuery):
    cart = db_client.select_products_from_cart(telegram_id=cd.from_user.id)
    print(cart)
    # if len(cart[0]) == 0:
    #     await cd.message.delete()
    #     await cd.message.answer("Корзина пуста, добавьте продукты", reply_markup=kb_client.main_menu())
    #     await cd.answer()
    # else:
    #     await cd.message.delete()
    #     await cd.message.answer(f"<b>Корзина:</b> {cart}", parse_mode=ParseMode.HTML)
    #     await cd.answer()