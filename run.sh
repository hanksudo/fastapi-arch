#!/bin/sh

PROJECT_PATH=$(pwd)/app

uvicorn main:app --port 3000 --reload --app-dir $PROJECT_PATH --reload-dir $PROJECT_PATH
