from src.settings import settings
from .config import bot, dp
from .handlers import router


async def start_bot():
    bot_token = settings.BOT_TOKEN
    webhook_path = f"/bot/{bot_token}"
    webhook_url = settings.DOMAIN + webhook_path
    await bot.set_webhook(url=webhook_url)
    dp.include_router(router)
