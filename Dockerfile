FROM mcr.microsoft.com/playwright/python:v1.24.0-focal

WORKDIR /app

RUN apt-get update && \
    apt-get install -y xvfb

COPY ./requirements.txt /app/

RUN python3 -m pip install pip -U && \
    pip install -r requirements.txt

COPY . /app/

ENTRYPOINT [ "/app/entrypoint.sh" ]