FROM python:3.9.7-slim

ARG APP_USER=appuser
RUN groupadd -r ${APP_USER} && useradd --no-log-init -r -g ${APP_USER} ${APP_USER}

RUN apt-get update
RUN apt-get install -y python3-pip libpq-dev python-dev
RUN python -m pip install --upgrade pip setuptools wheel

COPY . /src/

RUN pip install -r /src/requirements.txt
RUN pip install uwsgi

COPY app/uwsgi.ini /etc/uwsgi/
RUN chown -R www-data:www-data /src

WORKDIR /src
ENV PYTHONPATH="/src:/src/app:${PYTHONPATH}"
ENV PATH="/src:/src/app:${PATH}"
USER ${APP_USER}:${APP_USER}
