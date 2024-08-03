from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
from src.settings import settings


bot = Bot(token=settings.BOT_TOKEN)
memory = MemoryStorage()
dp = Dispatcher(storage=memory)
