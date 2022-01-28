FROM ubuntu:20.04

RUN apt-get update && apt-get install -y curl python3 python3-venv
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python3 -
ENV PATH $PATH:/root/.local/bin

COPY pyproject.toml ./
RUN poetry lock
RUN poetry install

COPY ./pdaj_project ./pdaj_project
WORKDIR ./pdaj_project

COPY run_django.sh ./
# RUN chmod +x run_server.sh
CMD ./run_django.sh