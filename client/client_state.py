from aiogram.filters.state import StatesGroup, State


class Client_main_state(StatesGroup):
    main_menu = State()

class Client_catalog_state(StatesGroup):
    category_menu = State()
    subcategory_menu = State()
    product_menu = State()
    adding_product_to_cart = State()

class Client_profile_state(StatesGroup):
    profile = State()


class Client_new_user_state(StatesGroup):
    phone_number = State()