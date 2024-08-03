from aiogram import Router, types

from src.bot.generators import get_messages_card

router = Router()


@router.message(lambda msg: msg.text == "Messages")
async def messages_list_handler(message: types.Message):
    card = get_messages_card(1)
    await message.answer(**card)
