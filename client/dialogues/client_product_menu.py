from aiogram.enums import ParseMode
from aiogram.types import CallbackQuery
from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.widgets.kbd import Button, Row, Group, ScrollingGroup
from aiogram_dialog.widgets.text import Const, Format, Multi, Jinja

from client.client_state import Client_catalog_state
from database_queries import db_queries


async def category_getter(**kwargs) -> dict:
    categories = db_queries.get_categories()
    if len(categories) == 0:
        return {}



dialog_product_menu = Dialog(
    Window(
        Const("<b>Выберите категорию</b>"),
        parse_mode="HTML",
        getter=category_getter,
        state=Client_catalog_state.category_menu

    )
)