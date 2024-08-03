from aiogram.utils.keyboard import InlineKeyboardButton
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup

from src.bot.keyboards import pagination_buttons
from src.db.config import messages_collection
from src.bot.config import PAGE_SIZE
from src.logger import logger as l
from src.paginators import paginated_messages


def get_messages_card(current_page):
    """
    Function to generate a reply keyboard with the messages.

    Parameters:
    current_page (int): The current page of messages.
    """
    messages = paginated_messages(current_page)
    messages_list = "".join(
        [
            f"{index}. {row['content'][:30]}... - **{row['timestamp']}**\n\n"
            for index, row in enumerate(messages["data"], start=1)
        ]
    )

    # Create a list of lists for the inline keyboard buttons
    keyboard = [
        InlineKeyboardButton(text=str(i), callback_data=f"message_detail:{row['id']}")
        for i, row in enumerate(messages["data"], start=1)
    ]

    # Add pagination buttons as a separate row
    l.info("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    l.info(messages_collection.count_documents({}))
    l.info(current_page)
    pagination = pagination_buttons(
        current_page,
        is_first=int(current_page) in [0, 1],
        is_last=messages_collection.count_documents({})
        < (int(current_page) + PAGE_SIZE),
    )
    # Combine the message buttons and pagination buttons
    messages_markup = InlineKeyboardMarkup(
        inline_keyboard=[keyboard, pagination],
        resize_keyboard=True,
    )
    return {"text": messages_list, "reply_markup": messages_markup}
