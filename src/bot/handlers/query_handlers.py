from aiogram import Router, types
import bson

from src.bot.generators import get_messages_card
from src.db.config import messages_collection
from src.bot.config import bot

router = Router()


@router.callback_query(
    lambda callback_query: callback_query.data.startswith("message_detail")
)
async def handle_message_detail(query: types.CallbackQuery):
    """
    This function handles the callback query for displaying detailed information of a selected message.

    Parameters:
    query (types.CallbackQuery): The callback query object containing the data and user information.

    Returns:
    None. This function is asynchronous and sends a message to the user.
    """
    # Extract the message ID from the callback data
    message_id = query.data.split(":")[1]

    # Fetch the details of the selected message from the MongoDB database
    message_details = messages_collection.find_one({"_id": bson.ObjectId(message_id)})
    # Create a formatted message with the details
    formatted_message = f"Message ID: {message_id}\nContent: {message_details['content']}\nSender: {message_details['sender']}\nTimestamp: {message_details['timestamp']}"

    # Send the formatted message as a reply to the user
    await bot.send_message(query.from_user.id, formatted_message)


@router.callback_query(lambda callback: callback.data.startswith("previous_page"))
async def previous_messages_pagination_handler(query: types.CallbackQuery):
    """
    Handles the callback query for navigating to the previous page of messages.

    Parameters:
    query (types.CallbackQuery): The callback query object containing the data and user information.
        The callback data should start with "previous_page:" followed by the current page number.

    Returns:
    None. This function is asynchronous and sends a message to the user with the previous page of messages.

    Extracts the current page from the callback data, fetches the previous page of messages from the MongoDB database,
    and sends the formatted message as a reply to the user.
    """
    # Extract the current page from the callback data
    previous_page = int(query.data.split(":")[1])

    # Fetch the previous page of messages from the MongoDB database
    await bot.send_message(query.from_user.id, **get_messages_card(previous_page))


@router.callback_query(lambda callback: callback.data.startswith("next_page"))
async def previous_messages_pagination_handler(query: types.CallbackQuery):
    """
    This function handles the callback query for navigating to the next page of messages.

    Parameters:
    query (types.CallbackQuery): The callback query object containing the data and user information.
        The callback data should start with "next_page:" followed by the current page number.

    Returns:
    None. This function is asynchronous and sends a message to the user with the next page of messages.
    """
    # Extract the current page from the callback data
    next_page = int(query.data.split(":")[1])

    # Fetch the previous page of messages from the MongoDB database
    await bot.send_message(query.from_user.id, **get_messages_card(next_page))
