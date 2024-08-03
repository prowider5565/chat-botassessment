from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardButton

from src.bot.keyboards import pagination_buttons
from src.db.config import messages_collection
from src.paginators import paginated_messages
from src.bot.config import PAGE_SIZE


def get_messages_card(current_page, **filters):
    """
    Generate a formatted message card with inline keyboard buttons for pagination and message details.

    Parameters:
    current_page (int): The current page number for pagination.

    Returns:
    dict: A dictionary containing the formatted message text and the inline keyboard markup.
    """
    messages = paginated_messages(current_page, **filters)
    messages_list = "".join(
        [
            f"{index}. <b>{row['content'][:30]}</b> - <em>{row['timestamp']}</em>\n\n"
            for index, row in enumerate(messages["data"], start=1)
        ]
    )

    # Create a list of lists for the inline keyboard buttons
    keyboard = [
        InlineKeyboardButton(text=str(i), callback_data=f"message_detail:{row['id']}")
        for i, row in enumerate(messages["data"], start=1)
    ]

    # Add pagination buttons as a separate row
    pagination = pagination_buttons(
        current_page,
        is_first=int(current_page) in [0, 1],
        is_last=messages_collection.count_documents({})
        < (int(current_page) * PAGE_SIZE),
    )
    # Combine the message buttons and pagination buttons
    messages_markup = InlineKeyboardMarkup(
        inline_keyboard=[keyboard, pagination],
        resize_keyboard=True,
    )
    return {"text": messages_list, "reply_markup": messages_markup}
