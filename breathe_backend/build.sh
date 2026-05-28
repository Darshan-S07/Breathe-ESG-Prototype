#!/usr/bin/env bash

cd breathe_backend

pip install -r requirements.txt

python manage.py collectstatic --noinput

python manage.py migrate
