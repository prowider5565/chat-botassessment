from fastapi import FastAPI
from src.api.handlers import router

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
logger.info("Including routers")
app.include_router(router, prefix="/messages")
