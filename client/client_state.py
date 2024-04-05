from aiogram.filters.state import StatesGroup, State


class ClientMainState(StatesGroup):
    main_menu = State()

class ClientCatalogState(StatesGroup):
    category_menu = State()
    subcategory_menu = State()
    product_menu = State()
    adding_product_to_cart = State()

class ClientProfileState(StatesGroup):
    profile = State()


class ClientNewUserState(StatesGroup):
    phone_number = State()