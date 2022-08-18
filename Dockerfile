FROM mcr.microsoft.com/playwright/python:v1.24.0-focal

ARG USER_ID

ARG GROUP_ID

RUN groupadd -g ${GROUP_ID} ci && \
    useradd --uid ${USER_ID} --gid ci \
        --shell /bin/bash --create-home ci && \
    install -d -m 0755 -o ci -g ci /app/artifacts && \
    chown --changes --silent --no-dereference --recursive \
        ${USER_ID}:${GROUP_ID} \
        /app/artifacts

WORKDIR /app

COPY ./requirements.txt .

RUN python3 -m pip install pip -U && \
    pip install -r requirements.txt

COPY . .

ENV PYTHONPATH=.

ENTRYPOINT [ "./entrypoint.sh" ]
