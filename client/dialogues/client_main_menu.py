from aiogram.enums import ParseMode
from aiogram.types import CallbackQuery
from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.text import Const, Format, Multi, Jinja

from client.client_state import Client_main_state, Client_profile_state



async def on_click_profile(callback_query: CallbackQuery,
                           button: Button,
                           dialog_manager: DialogManager
                           ) -> None:
    await dialog_manager.start(state=Client_profile_state.profile)


dialog_main = Dialog(
    Window(
        Const(text="<b>Главное меню</b>"),
        Row(
            Button(Const(text="Каталог"), id="_catalog"),
            Button(Const(text="Корзина"), id="_cart")
        ),
        Button(Const(text="Профиль"), id="_profile", on_click=on_click_profile),
        parse_mode=ParseMode.HTML,
        state=Client_main_state.main_menu
    )
)
