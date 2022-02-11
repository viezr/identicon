#!/bin/sh
set -e
if [ "$ENV" = 'DEV' ]; then
    echo "Running Development Server"
    exec python "identicon.py"
    #exec gunicorn --workers=4 --bind=0.0.0.0:9090 --reload identidock:app
elif [ "$ENV" = 'TEST' ]; then
    echo "Running tests..."
    exec python "tests_app_unit.py"
else
    echo "Running Production Server"
    exec gunicorn --workers=4 --bind=0.0.0.0:9090 identicon:app
fi
