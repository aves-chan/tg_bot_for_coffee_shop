from aiogram.fsm.state import State, StatesGroup

class Client_state(StatesGroup):
    start_order_state = State()

    """ Кофе """
    drinks_order_state = State()

    tea_order_state = State()
    coffee_order_state = State()

    """ Еда """
    meal_order_state = State()

    sandwich_order_state = State()
    breakfasts_order_state = State()

