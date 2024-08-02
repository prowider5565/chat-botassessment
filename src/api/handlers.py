from fastapi import FastAPI


application = FastAPI("/messages")


@application.get("/list")
async def list_messages_handler(request):
    """
    This function handles the GET request to list all messages.

    Parameters:
    request (Request): The FastAPI Request object containing information about the incoming request.

    Returns:
    dict: A dictionary containing a list of messages. The dictionary has the following structure:
        {
            "messages": [
                {
                    "id": int,
                    "content": str,
                    "sender": str,
                    "timestamp": str
                },
                ...
            ]
        }
    """
    # Fetch messages from MongoDB database
    messages = 
