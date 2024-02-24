from aiogram.enums import ParseMode, ContentType
from aiogram.types import CallbackQuery, Message
from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Row, RequestContact
from aiogram_dialog.widgets.markup.reply_keyboard import ReplyKeyboardFactory
from aiogram_dialog.widgets.text import Const, Format, Multi, Jinja

from client.client_state import Client_main_state, Client_new_user_state

async def handler_phone_number(message: Message,
                               message_input: MessageInput,
                               manager: DialogManager
                               ) -> None:
    await message.delete()
    await manager.start(Client_main_state.main_menu)


dialog_new_user = Dialog(
    Window(
        Const(text="<b>Перед использованием нужно отправить номер телефона</b>"),
        MessageInput(func=handler_phone_number, content_types=ContentType.CONTACT),
        RequestContact(Const(text="Отправить номер телефона")),
        parse_mode=ParseMode.HTML,
        markup_factory=ReplyKeyboardFactory(),
        state=Client_new_user_state.phone_number
    )
)
