from aiogram.exceptions import TelegramBadRequest


async def silent_delete_message(message):
    try:
        return await message.delete()
    except TelegramBadRequest:
        return
