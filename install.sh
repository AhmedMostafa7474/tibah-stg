#!/bin/bash

# Print commands and their arguments as they are executed.
set -x

# Check if python3 is installed
if ! command -v python3 &> /dev/null
then
    echo "python3 could not be found. Please install python3 and try again."
    exit 1
fi

# Check if pip3 is installed
if ! command -v pip3 &> /dev/null
then
    echo "pip3 could not be found. Please install pip3 and try again."
    exit 1
fi

# Check if virtual environment directory exists, if not, create one
if [ ! -d "env" ]; then
    python3 -m venv env
fi

# Activate the virtual environment
source env/bin/activate

# Install dependencies from requirements.txt
pip3 install -r requirements.txt

# Make migrations based on changes to models
python3 manage.py makemigrations

# Apply database migrations
python3 manage.py migrate

# Collect static files (optional, useful if you are serving static files from Django)
python3 manage.py collectstatic --noinput

# Run the Django development server
python3 manage.py runserver