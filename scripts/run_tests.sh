#! /bin/bash

echo "Activating the virtual environment..."
source .venv/Scripts/activate

echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

echo "Running Pytest on the project..."
pytest

echo "Deactivating the virtual environment..."
deactivate