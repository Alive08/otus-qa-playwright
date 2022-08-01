FROM mcr.microsoft.com/playwright/python:v1.24.0-focal

WORKDIR /app

COPY ./requirements.txt .

RUN python3 -m pip install pip -U && \
    pip install -r requirements.txt

COPY . .

ENV PYTHONPATH=.

ENTRYPOINT [ "./entrypoint.sh" ]
