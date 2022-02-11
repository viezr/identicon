#!/bin/sh
set -e
if [ "$ENV" = 'DEV' ]; then
    echo "Running Development Server"
    export FLASK_ENV=development
    exec python "identicon.py"
    #exec gunicorn --workers=4 --bind=0.0.0.0:9090 --reload identidock:app
else
    echo "Running Production Server"
    exec gunicorn --workers=4 --bind=0.0.0.0:9090 identicon:app
fi
