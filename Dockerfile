FROM python:3.8.5-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --system --deploy --ignore-pipfile
