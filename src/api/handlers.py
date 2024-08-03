from fastapi.exceptions import HTTPException
from fastapi.routing import APIRouter
from fastapi.responses import Response
from datetime import datetime
from fastapi import status
from typing import List

from src.db.config import messages_collection
from src.paginators import paginated_messages
from .schemas import Message
from .utils import utd, dtu


router = APIRouter()


@router.get("/list")
async def list_messages_handler(page: int = 1, count: int = 25):
    """
    This function handles the GET request to list all messages.


    Returns:
    dict: A dictionary containing a list of messages. The dictionary has the following structure:
        {
            "messages": [
                {
                    "id": str,
                    "content": str,
                    "sender": str,
                    "timestamp": int
                },
                ...
            ]
        }

    It is always recommended to return response with pagination, especially when data is massive
    and the response data contains list of rows. Otherwise, high traffic and memory may be used
    """
    if int(count) not in range(1, 600):
        raise HTTPException(
            detail="Data limit out of range. Min value: 1, Max value: 600",
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    # Fetch messages from MongoDB database in Pagination
    data = paginated_messages(page, count)
    return data


@router.post("/create", response_model=Message)
async def create_message_handler(message: Message):
    """
    This function handles the POST request to create a new message in the MongoDB database.

    Parameters:
    message (Message): An instance of the Message class containing the content, sender, and timestamp of the new message.

    Returns:
    dict: A dictionary representing the newly created message with the following structure:
        {
            "id": str,
            "content": str,
            "sender": str,
            "timestamp": int
        }
    """
    # Create a new message in MongoDB database
    content = message.content
    sender = message.sender
    timestamp = (
        dtu(message.timestamp)
        if message.timestamp
        else int(dtu(str(datetime.utcnow())))
    )
    # Save the message to the database and return its details in the response
    context = {"sender": sender, "content": content, "timestamp": timestamp}
    new_message_id = messages_collection.insert_one(context).inserted_id
    context["timestamp"] = utd(timestamp)
    return {**context, "id": str(new_message_id)}


@router.delete("/flush-all")
async def flush_all_messages_handler():
    """
    This function handles the DELETE request to delete all messages from the MongoDB database.

    Returns:
        No Content Response as success response
    """
    # Delete all messages from the database
    messages_collection.delete_many({})
    return Response(status_code=status.HTTP_204_NO_CONTENT)
