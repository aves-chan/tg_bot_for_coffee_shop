import typing

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters.callback_data import CallbackData

class Decrease_or_addition_callback_factory(CallbackData, prefix="AddDel"):
    action: str
    name: typing.Optional[str]
    count: typing.Optional[int]
    double_action: typing.Literal["T", "F"] = "F"
    """
    double_action: typing.Literal["T", "F"]  "T" == True, "F" == "False"
    """




class KB_client:
    def phone_number(self) -> ReplyKeyboardMarkup:
        button1 = [KeyboardButton(text="Отправить номер телефона", request_contact=True)]
        kb = ReplyKeyboardMarkup(keyboard=[button1], resize_keyboard=True)
        return kb

    def start_client(self) -> InlineKeyboardMarkup:
        button1 = [InlineKeyboardButton(text="Заказать", callback_data="Заказать")]
        kb = InlineKeyboardMarkup(inline_keyboard=[button1])
        return kb

    def generate_product_categories_or_menu_product(self,
            array: typing.List[str],
            categories_or_subcategories_or_products: typing.Literal["categories", "subcategories", "products"],
            back_button: str,
            page_number: int,
            page_number_next: int,
            page_number_previous: typing.Optional[int] = None
        ) -> InlineKeyboardMarkup:

        kb = InlineKeyboardBuilder()
        if categories_or_subcategories_or_products == "categories":
            for values in array:
                button = InlineKeyboardButton(text=values[0], callback_data=f"category_{values[0]}")
                kb.add(button)
        elif categories_or_subcategories_or_products == "subcategories":
            for values in array:
                button = InlineKeyboardButton(text=values[0], callback_data=f"subcategory_{values[0]}")
                kb.add(button)
        elif categories_or_subcategories_or_products == "products":
            for values in array:
                button = InlineKeyboardButton(text=values[0], callback_data=f"product_{values[0]}")
                kb.add(button)
        kb.adjust(2)
        if len(array) > 6:
            button1 = InlineKeyboardButton(text="<-", callback_data=f"page_category_{page_number_previous}")
            button2 = InlineKeyboardButton(text=f"№{page_number}📄", callback_data="ЭТА КНОПКА ВИЗУАЛЬНАЯ")
            button3 = InlineKeyboardButton(text="->", callback_data=f"page_category_{page_number_next}")
            button4 = InlineKeyboardButton(text=back_button, callback_data=back_button)
            if page_number == 0:
                kb.row(button2, button3, button4, width=3)
            else:
                kb.row(button1, button2, button3, button4, width=4)
        else:
            button1 = InlineKeyboardButton(text=back_button, callback_data=back_button)
            kb.row(button1, width=1)
        return kb.as_markup()

    def product_add_to_cart(self, product_array: typing.Tuple, product_quantity: int) -> InlineKeyboardMarkup:
        kb = InlineKeyboardBuilder()
        kb.button(text=f"Выбрали: {str(product_quantity)}", callback_data="ЭТА КНОПКА ВИЗУАЛЬНАЯ")
        kb.button(text="-2", callback_data=Decrease_or_addition_callback_factory(action="-", name=product_array[1], count=product_quantity, double_action="T"))
        kb.button(text="-1", callback_data=Decrease_or_addition_callback_factory(action="-", name=product_array[1], count=product_quantity, double_action="F"))
        kb.button(text="+1", callback_data=Decrease_or_addition_callback_factory(action="+", name=product_array[1], count=product_quantity, double_action="F"))
        kb.button(text="+2", callback_data=Decrease_or_addition_callback_factory(action="+", name=product_array[1], count=product_quantity, double_action="T"))
        if product_array[5] != None:
            kb.button(text=f"В наличии: {product_array[5]}", callback_data="ЭТА КНОПКА ВИЗУАЛЬНАЯ")
        kb.button(text="Добавить в корзину", callback_data=Decrease_or_addition_callback_factory(action="stop", name=product_array[1], count=product_quantity))
        kb.button(text="Назад", callback_data="Назад")
        kb.adjust(1, 4, 1, 1, 1)
        return kb.as_markup()

    def error_when_searching_for_subcategories(self, back_button: str) -> InlineKeyboardMarkup:
        button = [InlineKeyboardButton(text="Назад", callback_data=back_button)]
        kb = InlineKeyboardMarkup(inline_keyboard=[button])
        return kb

