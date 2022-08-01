FROM mcr.microsoft.com/playwright/python:v1.24.0-focal

ARG MY_UID

ARG MY_GID

WORKDIR /app

COPY ./requirements.txt .

RUN python3 -m pip install pip -U && \
    pip install -r requirements.txt

COPY . .

ENV PYTHONPATH=.

RUN groupadd --gid ${MY_GID} ci \
    && useradd --uid ${MY_UID} --gid ci \
    --shell /bin/bash --create-home ci

ENTRYPOINT [ "./entrypoint.sh" ]
