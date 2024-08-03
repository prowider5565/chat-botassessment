from pydantic import BaseModel, Field
from typing import Optional


class Message(BaseModel):
    """
    A class representing a message with attributes: id, content, sender, and timestamp.

    Attributes:
    id (UUID4): The unique identifier of the message.
    content (str): The content of the message.
    sender (str): The sender of the message.
    timestamp (int): The timestamp of when the message was sent.
    """

    id: Optional[str] = Field(None, description="The unique identifier of the message")
    content: str
    sender: int
    timestamp: Optional[str] = Field(
        None, description="The timestamp of when the message was sent"
    )
