from aiogram.fsm.context import FSMContext
from aiogram import Router, types
from datetime import datetime

from src.bot.generators import get_messages_card
from src.db.config import messages_collection
from src.bot.states import MessageState
from src.api.utils import dtu

router = Router()


@router.message(lambda msg: msg.text == "Messages")
async def messages_list_handler(message: types.Message):
    card = get_messages_card(1)
    await message.answer(**card)


@router.message(lambda msg: msg.text == "Create Message")
async def previous_page_handler(message: types.Message, state: FSMContext):
    await message.answer("Please enter your message")
    await state.set_state(MessageState.content)


@router.message(MessageState.content)
async def content_handler(message: types.Message, state: FSMContext):
    """
    This function handles the creation of a new message. It extracts the necessary information from the received message,
    creates a context dictionary, saves the message to the database, resets the state, and sends a success message.

    Parameters:
    message (types.Message): The received message containing the content of the new message.
    state (FSMContext): The current state of the conversation, used to reset the state after message creation.

    Returns:
    Success Message
    """
    timestamp = dtu(
        str(datetime.utcnow())
    )  # Get the current timestamp in a specific format using the dtu function.
    sender = message.from_user.id  # Get the ID of the sender from the received message.
    content = message.text  # Get the content of the message from the received message.

    # Create a context dictionary containing the sender, content, and timestamp.
    context = {"sender": sender, "content": content, "timestamp": timestamp}

    # Save the message to the database using the messages_collection.
    messages_collection.insert_one(context)

    # Reset the state of the conversation using the state.clear() method.
    await state.clear()

    # Send a success message to the user, removing the reply keyboard.
    await message.answer(
        "Message created successfully",
        reply_markup=types.ReplyKeyboardRemove(),
    )


# @router.message(lambda msg: msg.text == "My Messages")
# async def my_messages_handler(message: types.Message):
#     """
#     This function handles the initial request for the user's messages. It sets the current page to 1,
#     fetches the messages from the database, and sends them as a card with pagination buttons.

#     Parameters:
#     message (types.Message): The received message containing the user's ID.

#     Returns:
#     Messages card with pagination buttons
#     """
#     current_page = 1
#     messages_card = get_messages_card(
#         current_page, filters={"sender": message.from_user.id}
#     )
#     await message.answer()
