from aiogram.utils.keyboard import ReplyKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.types.inline_keyboard_button import InlineKeyboardButton


get_button = KeyboardButton(text="Messages")
create_button = KeyboardButton(text="Create Message")
# my_messages_button = KeyboardButton(text="My Messages")
user_menu = ReplyKeyboardMarkup(
    keyboard=[[get_button, create_button]],
    resize_keyboard=True,
)


def pagination_buttons(current_page, is_last, is_first):
    buttons = []
    if not is_first:
        buttons.append(
            InlineKeyboardButton(
                text="<< Previous", callback_data=f"previous_page:{current_page - 1}"
            )
        )
    if not is_last:
        buttons.append(
            InlineKeyboardButton(
                text="Next >>", callback_data=f"next_page:{current_page + 1}"
            )
        )
    return buttons
