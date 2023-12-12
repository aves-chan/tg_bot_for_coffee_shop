from aiogram.fsm.state import State, StatesGroup

class Client_state(StatesGroup):
    start_order_state = State()

    drinks_order_state = State()

    tea_order_state = State()
    coffee_order_state = State()

