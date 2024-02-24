from aiogram.filters.state import StatesGroup, State


class Client_main_state(StatesGroup):
    main_menu = State()


class Client_profile_state(StatesGroup):
    profile = State()


class Client_new_user_state(StatesGroup):
    phone_number = State()