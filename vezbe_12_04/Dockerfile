FROM python:3.8-buster

WORKDIR /usr/src

COPY . /usr/src/

RUN apt update && pip install poetry
RUN poetry install

CMD poetry shell