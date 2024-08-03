import pymongo

from src.settings import settings


mongo_client = pymongo.MongoClient(
    host=settings.MONGO_HOST,
    port=27017,
    tz_aware=settings.MONGO_TZ_AWARE,
)
mongo_db = mongo_client[settings.MONGO_NAME]
messages_collection = mongo_db["messages"]
