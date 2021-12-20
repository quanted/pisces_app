FROM python:3.9.7-slim

ARG APP_USER=appuser
RUN groupadd -r ${APP_USER} && useradd --no-log-init -r -g ${APP_USER} ${APP_USER}

RUN apt-get update
RUN apt-get install -y python3-pip libpq-dev python-dev
RUN python -m pip install --upgrade pip setuptools wheel

COPY . /src/pisces_app

RUN pip install -r /src/pisces_app/requirements.txt
RUN pip install uwsgi

COPY app/uwsgi.ini /etc/uwsgi/
RUN chown -R www-data:www-data /src

WORKDIR /src/pisces_app
ENV PYTHONPATH="/src:/src/pisces_app:${PYTHONPATH}"
ENV PATH="/src:/src/pisces_app:${PATH}"
USER ${APP_USER}:${APP_USER}
