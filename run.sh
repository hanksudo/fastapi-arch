#!/bin/sh

PROJECT_PATH=$(pwd)/app

export PYTHONPATH=.

poetry run uvicorn main:app \
    --port 8000 \
    --reload \
    --app-dir $PROJECT_PATH \
    --reload-dir $PROJECT_PATH