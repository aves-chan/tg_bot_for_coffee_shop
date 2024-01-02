import json

from aiogram import Router, types, F
from aiogram.enums import ParseMode

from handlers.handlers_client.handlers_client_for_adding_user_to_database.handlers_registration_user import client_registration_router
from sql_queries.db_client import DB_client
from keyboard.keyboard_client import KB_client, Decrease_or_addition_callback_factory

client_product_menu_router = Router()
client_product_menu_router.include_routers(client_registration_router)

kb_client = KB_client()

db_client = DB_client()

@client_product_menu_router.callback_query(F.data == "Заказать")
async def handler_client_creating_product_categories(cd: types.CallbackQuery):
    categories = db_client.select_categories()
    if len(categories) == 0:
        await cd.message.delete()
        await cd.message.answer(text="Ошибка,к сожалению нет категорий. Попробуйте позже",
                                reply_markup=kb_client.start_client())
        await cd.answer()
    else:
        await cd.message.edit_text(text="<b>Выбери категорию</b>",
                                   parse_mode=ParseMode.HTML,
                                   reply_markup=kb_client.generate_product_categories_or_menu_product(array=categories,
                                                                                                      categories_or_subcategories_or_products="categories",
                                                                                                      back_button="Назад к главному меню",
                                                                                                      page_number=0,
                                                                                                      page_number_next=6))
        await cd.answer()

@client_product_menu_router.callback_query(F.data == "Назад к категориям")
async def handler_client_back_to_categories_button(cd: types.CallbackQuery):
    await cd.message.delete()
    await cd.message.answer(text="Пока не сделано", reply_markup=kb_client.start_client())
    await cd.answer(show_alert=True, text="handler_client_back_to_categories_button\n\nэтот обработчик реагирует")

@client_product_menu_router.callback_query(F.data.regexp('page_category_\d+'))
async def handler_client_page_categories(cd: types.CallbackQuery):
    await cd.message.delete()
    await cd.message.answer("Пока не сделано")
    await cd.answer(show_alert=True, text="handler_client_page_categories\n\nэтот обработчик реагирует")

@client_product_menu_router.callback_query(F.data.regexp('category_\w+'))
async def handler_client_creating_product_subcategories(cd: types.CallbackQuery):
    data = cd.data[9:]
    subcategories = db_client.select_subcategories(data)
    if len(subcategories) == 0:
        await cd.message.delete()
        await cd.message.answer(text="Ошибка, к сожалению не смог найти категорию. Попробуйте позже или другую категорию",
                                reply_markup=kb_client.error_when_searching_for_subcategories(back_button="Назад к категориям"))
        await cd.answer()
    else:
        await cd.message.edit_text(text=f"Категория <b>{data}</b>",
                                   parse_mode=ParseMode.HTML,
                                   reply_markup=kb_client.generate_product_categories_or_menu_product(array=subcategories,
                                                                                                      categories_or_subcategories_or_products="subcategories",
                                                                                                      back_button="Назад к категориям",
                                                                                                      page_number=0,
                                                                                                      page_number_next=6))
        await cd.answer()

@client_product_menu_router.callback_query(F.data.regexp('subcategory_\w+'))
async def handler_client_creating_product_menu(cd: types.CallbackQuery):
    data = cd.data[12:]
    products = db_client.select_products(data)
    if len(products) == 0:
        await cd.message.delete()
        await cd.message.answer(text="Ошибка, к сожалению не смог найти подкатегорию. Попробуйте позже или другую подкатегорию",
                                reply_markup=kb_client.error_when_searching_for_subcategories(back_button="Назад к категориям"))
        await cd.answer()
    else:
        await cd.message.edit_text(text=f"Подкатегория <b>{data}</b>",
                                   parse_mode=ParseMode.HTML,
                                   reply_markup=kb_client.generate_product_categories_or_menu_product(array=products,
                                                                                                      categories_or_subcategories_or_products="products",
                                                                                                      back_button="Назад к категоиям",
                                                                                                      page_number=0,
                                                                                                      page_number_next=6))
        await cd.answer()

@client_product_menu_router.callback_query(F.data.regexp('product_\w+'))
async def handler_client_adds_in_cart_product(cd: types.CallbackQuery):
    data = cd.data[8:]
    product = db_client.select_product(data)
    if product == None:
        await cd.message.delete()
        await cd.message.answer(text="Ошибка, к сожалению не смог найти продукт. Попробуйте позже или другой продукт",
                                reply_markup=kb_client.error_when_searching_for_subcategories(back_button="Назад к категориям"))
        await cd.answer()
    else:
        if product[2] == None:
            await cd.message.edit_text(text=f"""
<b>Продукт:</b> {product[1]}

<b>Описание:</b> {product[3]}

<b>Цена:</b> {product[4]}p
            """,
            parse_mode=ParseMode.HTML,
            reply_markup=kb_client.product_add_to_cart(product_array=product, product_quantity=1))
        else:
            await cd.message.delete()
            await cd.message.answer("Пока не сделано")
            await cd.answer(show_alert=True, text="handler_client_adds_in_cart_product\n\nэтот обработчик реагирует")

@client_product_menu_router.callback_query(Decrease_or_addition_callback_factory.filter())
async def handler_client_decrease_or_addition_product(cd: types.CallbackQuery, callback_data: Decrease_or_addition_callback_factory):
    product = db_client.select_product(name_product=callback_data.name)
    if callback_data.action == "-":
        if callback_data.double_action == "T":
            product_quantity = callback_data.count - 2
            if product_quantity < 1:
                await cd.answer(
                    text="Минимальное значение может быть 1. Eсли Вы хотите выйти не добавив продукта нажмите кнопку назад",
                    show_alert=True)
            else:
                await cd.message.edit_reply_markup(
                    reply_markup=kb_client.product_add_to_cart(product_array=product,
                                                               product_quantity=product_quantity))
                await cd.answer()
        elif callback_data.double_action == "F":
            if callback_data.count <= 1:
                await cd.answer(
                    text="Минимальное значение может быть 1. Eсли Вы хотите выйти не добавив продукта нажмите кнопку назад",
                    show_alert=True)
            else:
                product_quantity = callback_data.count - 1
                await cd.message.edit_reply_markup(reply_markup=kb_client.product_add_to_cart(product_array=product,
                                                                                              product_quantity=product_quantity))
                await cd.answer()

    elif callback_data.action == "+":
        if callback_data.double_action == "T":
            product_quantity = callback_data.count + 2
            if product_quantity > 15:
                await cd.answer(text="Максимальное значение может быть 15",
                                show_alert=True)
            else:
                await cd.message.edit_reply_markup(
                    reply_markup=kb_client.product_add_to_cart(product_array=product, product_quantity=product_quantity))
                await cd.answer()
        elif callback_data.double_action == "F":
            if callback_data.count >= 15:
                await cd.answer(text="Максимальное значение может быть 15",
                                show_alert=True)
            else:
                product_quantity = callback_data.count + 1
                await cd.message.edit_reply_markup(reply_markup=kb_client.product_add_to_cart(product_array=product, product_quantity=product_quantity))
                await cd.answer()

    elif callback_data.action == "stop":
        client_cart = db_client.select_client_cart(cd.from_user.id)
        if client_cart[0] == None:
            dict_cart = {product[1]: callback_data.count}
            json_cart = json.dumps(dict_cart)
            db_client.change_in_cart(telegram_id=cd.from_user.id, new_cart=json_cart)
            print(db_client.select_client_cart(telegram_id=cd.from_user.id))


