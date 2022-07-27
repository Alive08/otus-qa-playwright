FROM mcr.microsoft.com/playwright/python:v1.24.0-focal

WORKDIR /app

RUN apt-get update && \
    apt-get install -y xvfb
    # apt-get install -y xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic

COPY ./requirements.txt /app/

RUN python3 -m pip install pip -U && \
    pip install -r requirements.txt

COPY . /app/

CMD [ "/bin/bash" ]

# ENTRYPOINT [ "xvfb-run", "--auto-servernum", "--server-num=1", "--server-args='-screen 0, 1920x1080x24'", "pytest", "--headed", "--base-url=http://example.com" ]
