from datetime import datetime


def utd(unix_timestamp):
    """
    Convert a Unix timestamp to a human-readable date.

    Parameters:
    unix_timestamp (int): Unix timestamp to be converted.

    Returns:
    str: Human-readable date in the format YYYY-MM-DD HH:MM:SS.
    """
    return datetime.utcfromtimestamp(unix_timestamp).strftime("%Y-%m-%d %H:%M:%S")


def dtu(date_str, date_format="%Y-%m-%d %H:%M:%S"):
    """
    Convert a human-readable date to a Unix timestamp.

    Parameters:
    date_str (str): Date string to be converted.
    date_format (str): Format of the input date string. Default is '%Y-%m-%d %H:%M:%S'.

    Returns:
    int: Unix timestamp.
    """
    # Check for fractional seconds and handle them appropriately
    if "." in date_str:
        date_format += ".%f"
    dt = datetime.strptime(date_str, date_format)
    return int(dt.timestamp())
