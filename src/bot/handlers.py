from aiogram import types, Router
from aiogram.filters import Command

from src.paginators import paginated_messages


router = Router()


@router.message(Command("start"))
async def fetch_messages(message: types.Message):
    # Fetch messages from the MongoDB database
    messages = paginated_messages(1, count=25)

    # Send fetched messages as a reply to the user
    await message.answer(str(messages))
