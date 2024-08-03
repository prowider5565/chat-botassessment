from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
from src.settings import settings


bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
memory = MemoryStorage()
dp = Dispatcher(storage=memory)
PAGE_SIZE = 2
