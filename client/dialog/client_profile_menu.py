from aiogram.types import CallbackQuery
from aiogram_dialog import (
    Dialog, Window, DialogManager,
)
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.text import Const, Format

from client.client_state import ClientMainState, ClientProfileState
from database_queries import db_queries

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
    await dialog_manager.start(state=ClientMainState.main_menu)


async def getter_profile(dialog_manager: DialogManager, **kwargs):
    user = db_queries.get_profile(telegram_id=dialog_manager.event.from_user.id)
    return {
        "first_name": user.firstname,
        "username": user.username,
        "user_id": user.telegram_id,
        "phone_number": user.phone_number
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
        state=ClientProfileState.profile
    )
)
