#!/usr/bin/env bash

# Install Poetry if not already installed
curl -sSL https://install.python-poetry.org | python3 -

# Install dependencies via Poetry
poetry install

# Run migrations and start the server
poetry run python manage.py migrate
poetry run python manage.py runserver 0.0.0.0:8000
