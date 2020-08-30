FROM python:3.8.5-slim

WORKDIR /usr/src/app

COPY Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "./app.py" ]
