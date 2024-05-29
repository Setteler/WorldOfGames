# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

RUN pip install -r requirements.txt


# Make port 8777 available to the world outside this container
EXPOSE 8777


# Define environment variable
# ENV NAME WorldOfGames

# Run MainScores.py when the container launches
CMD ["python", "MainScores.py"]

# Copy Scores.txt to the container
COPY Scores.txt /Scores.txt
