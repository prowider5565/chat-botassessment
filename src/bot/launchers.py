from src.settings import settings
from .config import bot, dp
from .handlers.commands import router as commands_router
from .handlers.message_handlers import router as messages_router
from .handlers.query_handlers import router as query_router


async def start_bot():
    bot_token = settings.BOT_TOKEN
    webhook_path = f"/bot/{bot_token}"
    webhook_url = settings.DOMAIN + webhook_path
    await bot.set_webhook(url=webhook_url)
    dp.include_router(commands_router)
    dp.include_router(messages_router)
    dp.include_router(query_router)
