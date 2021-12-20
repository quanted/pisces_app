#!/bin/bash
python /src/pisces_app/manage.py collectstatic --noinput
python /src/pisces_app/manage.py migrate
exec uwsgi /etc/uwsgi/uwsgi.ini
