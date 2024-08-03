# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /code

# Copy the current directory contents into the container at /code
COPY . /code

# Copy the .env file into the container
COPY .env /code/.env

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

EXPOSE 8000

# Run app.py when the container launches
ENTRYPOINT ["sh", "-c", "sh ./launcher.sh"]

