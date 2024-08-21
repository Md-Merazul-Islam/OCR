# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Install Tesseract OCR and other necessary packages
RUN apt-get update && apt-get install -y tesseract-ocr libtesseract-dev libleptonica-dev

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies using Poetry (or pip if you're not using Poetry)
RUN pip install --no-cache-dir poetry
RUN poetry install --no-root

# Expose the port that the app runs on
EXPOSE 8000

# Command to run the application
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
