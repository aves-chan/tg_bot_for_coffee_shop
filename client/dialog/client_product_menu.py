import typing

from aiogram.enums import ParseMode
from aiogram.types import CallbackQuery
from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.widgets.kbd import Button, Row, Group, ScrollingGroup, Cancel
from aiogram_dialog.widgets.text import Const, Format, Multi, Jinja

from client.client_state import ClientCatalogState
from database_queries import db_queries


def generate_category_menu_buttons() -> typing.List:
    buttons = []
    for i in range(100):
        i = str(i)
        buttons.append(Button(Const(i), id=i))
    return buttons


category_menu_buttons = generate_category_menu_buttons()


dialog_product_menu = Dialog(
    Window(
        Const("<b>Выберите категорию</b>"),
        Group(
            ScrollingGroup(
                *category_menu_buttons,
                id="category_menu",
                width=2,
                height=6
            ),
            Cancel(text=Const(text="Назад"))
        ),
        parse_mode="HTML",
        state=ClientCatalogState.category_menu

    )
)