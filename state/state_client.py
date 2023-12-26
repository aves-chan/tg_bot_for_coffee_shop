from aiogram.fsm.state import State, StatesGroup

class Client_state(StatesGroup):
    start_order_state = State()

    """ Напитки """
    drinks_order_state = State()

    tea_order_state = State()
    coffee_order_state = State()

    """ Еда """
    meal_order_state = State()

    breakfasts_quantity_selection_state = State()
    sandwich_quantity_selection_state = State()
    breakfasts_quantity_selection2_state= State()
    sandwich_quantity_selection2_state = State()

