import typing

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


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


    def product_add_to_cart(self, array_products: typing.Tuple) -> InlineKeyboardMarkup:
        button1 = InlineKeyboardButton(text="-", callback_data="-")
        button2 = InlineKeyboardButton(text="1", callback_data="ЭТА КНОПКА ВИЗУАЛЬНАЯ")
        button3 = InlineKeyboardButton(text="+", callback_data="+")
        button4 = InlineKeyboardButton(text=f"В наличии: {array_products[5]}", callback_data="ЭТА КНОПКА ВИЗУАЛЬНАЯ")
        button5 = InlineKeyboardButton(text="Добавить в корзину", callback_data="Добавить")
        button6 = InlineKeyboardButton(text="Назад", callback_data="Назад")
        kb = InlineKeyboardMarkup(inline_keyboard=[[button1, button2, button3],[button4],[button5],[button6]])
        return kb

    def error_when_searching_for_subcategories(self, back_button: str) -> InlineKeyboardMarkup:
        button = [InlineKeyboardButton(text="Назад", callback_data=back_button)]
        kb = InlineKeyboardMarkup(inline_keyboard=[button])
        return kb
