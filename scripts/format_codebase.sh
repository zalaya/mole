#! /bin/bash

source .venv/Scripts/activate

pip install -r requirements.txt

black ./src
black ./tests

deactivate