from fastapi import FastAPI
from aiogram import types
import logging

from src.api.handlers import router
from src.bot.launchers import start_bot
from src.settings import settings
from src.bot.config import dp, bot

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
logger.info("Including routers")
app.include_router(router, prefix="/messages")


@app.on_event("startup")
async def startup_handler():
    logger.info("Starting up...")
    await start_bot()


@app.post(f"/bot/{settings.BOT_TOKEN}")
async def bot_webhook_handler(update: dict):
    telegram_update = types.Update(**update)
    await dp.feed_update(bot=bot, update=telegram_update)
