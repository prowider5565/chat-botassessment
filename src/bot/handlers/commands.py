from aiogram import types, Router
from aiogram.filters import Command

from src.bot.keyboards import user_menu


router = Router()


@router.message(Command("start"))
async def fetch_messages(message: types.Message):
    await message.answer(
        f"Welcome {message.from_user.full_name}, glad to see you here!!!",
        reply_markup=user_menu,
    )
