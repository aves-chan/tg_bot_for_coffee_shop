from aiogram.types import Message, CallbackQuery

from aiogram.types import CallbackQuery
from aiogram_dialog import (
    Dialog, Window, DialogManager,
)
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.text import Const, Format, Multi

from client.client_state import Client_main_state, Client_profile_state


message_text_for_profile = """
Имя: {first_name}

Имя в телеграм: {username}

Id: {user_id}

Номер телефона: {phone_number}
"""


async def on_click_back(callback_query: CallbackQuery,
                        button: Button,
                        dialog_manager: DialogManager
                        ) -> None:
    await dialog_manager.start(state=Client_main_state.main_menu)


async def getter_profile(dialog_manager: DialogManager, **kwargs):
    return {
        "first_name": dialog_manager.event.from_user.first_name,
        "username": dialog_manager.event.from_user.username,
        "user_id": dialog_manager.event.from_user.id,
        "phone_number": "None",
    }

dialog_profile = Dialog(
    Window(
        Format(text=message_text_for_profile),
        Row(
            Button(Const(text="Реф ссылка"), id="_referral_link"),
            Button(Const(text="Мои заказы"), id="_orders")
        ),
        Row(
            Button(Const(text="Назад"), id="_back", on_click=on_click_back),
            Button(Const(text="Корзина"), id="_cart")
        ),
        getter=getter_profile,
        state=Client_profile_state.profile
    )
)
