FROM python:3.8.5-slim

WORKDIR /usr/src/app

COPY Pipfile.lock ./
RUN python -m pip install pipenv
RUN pipenv shell
RUN pipenv install --ignore-pipfile

COPY . .

CMD [ "python", "./app.py" ]
