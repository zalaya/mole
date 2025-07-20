#! /bin/bash

echo "Activating the virtual environment..."
source .venv/Scripts/activate

echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

echo "Running Black on the 'src' directory..."
black ./src

echo "Deactivating the virtual environment..."
deactivate