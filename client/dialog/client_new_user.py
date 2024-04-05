from aiogram.enums import ParseMode, ContentType
from aiogram.types import Message
from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import RequestContact
from aiogram_dialog.widgets.markup.reply_keyboard import ReplyKeyboardFactory
from aiogram_dialog.widgets.text import Const

from database_queries import db_queries
from client.client_state import ClientMainState, ClientNewUserState

async def handler_phone_number(message: Message,
                               message_input: MessageInput,
                               manager: DialogManager
                               ) -> None:
    db_queries.add_new_user(telegram_id=message.from_user.id,
                            firstname=message.from_user.first_name,
                            username=message.from_user.username,
                            phone_number=message.contact.phone_number)
    await manager.start(ClientMainState.main_menu)


dialog_new_user = Dialog(
    Window(
        Const(text="<b>Перед использованием нужно отправить номер телефона</b>"),
        MessageInput(func=handler_phone_number, content_types=ContentType.CONTACT),
        RequestContact(Const(text="Отправить номер телефона")),
        parse_mode=ParseMode.HTML,
        markup_factory=ReplyKeyboardFactory(),
        state=ClientNewUserState.phone_number
    )
)
