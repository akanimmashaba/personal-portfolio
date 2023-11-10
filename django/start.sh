#!/bin/bash 

python manage.py makemigrations --no-input
python manage.py migrate --no-input

gunicorn --bind 0.0.0.0:80010 config.wsgi --daemon