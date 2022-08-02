FROM mcr.microsoft.com/playwright/python:v1.24.0-focal

WORKDIR /app

COPY ./requirements.txt .

RUN chown pwuser:pwuser /app && chmod 775 /app && \
    python3 -m pip install pip -U && \
    pip install -r requirements.txt

COPY . .

ENV PYTHONPATH=.

# RUN groupadd --gid ${MY_GID} ci \
#     && useradd --uid ${MY_UID} --gid ci \
#     --shell /bin/bash --create-home ci

ENTRYPOINT [ "./entrypoint.sh" ]
