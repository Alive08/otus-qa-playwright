FROM alpine

RUN set -xe; \
    apk add --update xvfb;\
    rm -rf /var/cache/apk/*;

ENV DISPLAY 99

ADD entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/bin/sh", "/entrypoint.sh"]

