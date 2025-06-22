#!/usr/bin/env bash

# Migraciones y archivos estáticos
python manage.py migrate
python manage.py collectstatic --noinput

