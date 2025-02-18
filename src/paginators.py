from src.db.config import messages_collection
from src.bot.config import PAGE_SIZE
from .api.utils import utd


def paginated_messages(page, count=PAGE_SIZE, **filters):
    """
    Function to paginate messages in the MongoDB database.

    Parameters:
    page (int): The page number to fetch.
    count (int, optional): The number of messages per page. Defaults to 25.

    Returns:
    list: A list of messages for the given page.
    """
    messages = [
        {
            "content": message["content"],
            "sender": message["sender"],
            "timestamp": utd(message["timestamp"]),
            "id": str(message["_id"]),
        }
        for message in list(
            messages_collection.find(filters).skip((page - 1) * count).limit(count)
        )
    ]
    data = {"data": messages, "count": len(messages), "page": page}
    return data
