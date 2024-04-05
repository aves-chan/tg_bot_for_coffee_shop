from aiogram.types import CallbackQuery
from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.text import Const

from client.client_state import ClientMainState, ClientProfileState, ClientCatalogState


async def on_click_catalog(callback_query: CallbackQuery,
                           button: Button,
                           dialog_manager: DialogManager
                           ) -> None:
    await dialog_manager.start(state=ClientCatalogState.category_menu)


async def on_click_profile(callback_query: CallbackQuery,
                           button: Button,
                           dialog_manager: DialogManager
                           ) -> None:
    await dialog_manager.start(state=ClientProfileState.profile)


dialog_main = Dialog(
    Window(
        Const(text="<b>Главное меню</b>"),
        Row(
            Button(Const(text="Каталог"), id="_catalog", on_click=on_click_catalog),
            Button(Const(text="Корзина"), id="_cart")
        ),
        Button(Const(text="Профиль"), id="_profile", on_click=on_click_profile),
        parse_mode="HTML",
        state=ClientMainState.main_menu
    )
)
