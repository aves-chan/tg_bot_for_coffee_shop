from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def kb_phone_number():
    button1 = [KeyboardButton(text="Отправить номер телефона", request_contact=True)]
    kb = ReplyKeyboardMarkup(keyboard=[button1], resize_keyboard=True)
    return kb


def kb_start_client():
    button1 = [InlineKeyboardButton(text="Заказать", callback_data="Заказать")]
    kb = InlineKeyboardMarkup(inline_keyboard=[button1])
    return kb

def kb_order_main_menu():
    button1 = InlineKeyboardButton(text="Напитки 🥤", callback_data="Напитки")
    button2 = InlineKeyboardButton(text="Еда 🥪", callback_data="Еда")
    button3 = InlineKeyboardButton(text="Десерты 🍰", callback_data="Десерты")
    button4 = InlineKeyboardButton(text="Корзина 🧺", callback_data="Корзина")
    kb = InlineKeyboardMarkup(inline_keyboard=[[button1], [button2, button3], [button4]])
    return kb


""" ЕДА """
def kb_order_meal_category():
    button1 = InlineKeyboardButton(text="Завтраки", callback_data="Завтраки")
    button2 = InlineKeyboardButton(text="Сэндвичи", callback_data="Сэндвичи")
    button3 = InlineKeyboardButton(text="Назад к главному меню", callback_data="Назад к главному меню")
    kb = InlineKeyboardMarkup(inline_keyboard=[[button1, button2], [button3]])
    return kb

def kb_generating_sandwich_buttons(array_meal):
    kb = InlineKeyboardBuilder()
    for values in array_meal:
        kb.button(text=values[1], callback_data=str(values[0]))
    kb.adjust(2)
    return kb

def kb_generating_breakfasts_buttons(array_meal):
    kb = InlineKeyboardBuilder()
    for values in array_meal:
        kb.button(text=values[1], callback_data=str(values[0]))
    kb.adjust(2)
    return kb

def adding_to_cart_meal(array_meal):
    button1 = InlineKeyboardButton(text="-", callback_data="-")
    button2 = InlineKeyboardButton(text="1", callback_data="ЭТА КНОПКА ВИЗУАЛЬНАЯ")
    button3 = InlineKeyboardButton(text="+", callback_data="+")
    button4 = InlineKeyboardButton(text=f"В наличии: {array_meal[5]}", callback_data="ЭТА КНОПКА ВИЗУАЛЬНАЯ")
    button5 = InlineKeyboardButton(text="Добавить в корзину", callback_data="Добавить")
    button6 = InlineKeyboardButton(text="Назад", callback_data="Назад")
    kb = InlineKeyboardMarkup(inline_keyboard=[[button1, button2, button3],[button4],[button5],[button6]])
    return kb

"""КОНЕЦ ЕДЫ """



""" НАПИТКИ """

def kb_order_drinks_category():
    button1 = InlineKeyboardButton(text="Кофе", callback_data="Кофе")
    button2 = InlineKeyboardButton(text="Чай", callback_data="Чай")
    button3 = InlineKeyboardButton(text="Назад к главному меню", callback_data="Назад к главному меню")
    kb = InlineKeyboardMarkup(inline_keyboard=[[button1, button2], [button3]])
    return kb

def kb_order_drinks_coffee():
    button1 = InlineKeyboardButton(text="Капучино", callback_data="Капучино")
    button2 = InlineKeyboardButton(text="Латте", callback_data="Латте")
    button3 = InlineKeyboardButton(text="Флет уйат", callback_data="Флет уйат")
    button4 = InlineKeyboardButton(text="Амрерикано", callback_data="Амрерикано")
    button5 = InlineKeyboardButton(text="Эспрессо", callback_data="Эспрессо")
    button6 = InlineKeyboardButton(text="Назад к выбору напитков", callback_data="Назад к выбору напитков")
    kb = InlineKeyboardMarkup(inline_keyboard=[[button1, button2], [button3, button4], [button5], [button6]])
    return kb

def kb_order_drinks_tea():
    button1 = InlineKeyboardButton(text="Зеленый", callback_data="Зеленый")
    button2 = InlineKeyboardButton(text="Черный", callback_data="Черный")
    button3 = InlineKeyboardButton(text="Красный", callback_data="Красный")
    button4 = InlineKeyboardButton(text="Цветочный", callback_data="Цветочный")
    button5 = InlineKeyboardButton(text="Фирменный", callback_data="Фирменный")
    button6 = InlineKeyboardButton(text="Назад к выбору напитков", callback_data="Назад к выбору напитков")
    kb = InlineKeyboardMarkup(inline_keyboard=[[button1, button2], [button3, button4], [button5], [button6]])
    return kb

""" КОНЕЦ НАПИТКОВ """