FROM python:3.7.4-alpine3.10

MAINTAINER SHI TAO <shitao0418@gamil.com>

ENV LIBRARY_PATH=/lib:/usr/lib

ENV RUNTIME_PACKAGES ca-certificates libxslt libxml2 libpq
ENV BUILD_PACKAGES build-base libxslt-dev libxml2-dev libffi-dev openssl-dev postgresql-dev

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories && \
    apk update && \
    apk upgrade && \
    apk add --no-cache --update ${RUNTIME_PACKAGES} ${BUILD_PACKAGES} && \
    pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip --no-cache-dir install --upgrade \
        scrapy \
        scrapy-redis \
        scrapyd \
        logparser \
        beautifulsoup4 \
        lxml \
        html5lib && \
    mkdir -p /etc/scrapyd/eggs/ && \
    mkdir -p /etc/scrapyd/logs/ && \
    mkdir -p /etc/scrapyd/items/ && \
    mkdir -p /etc/scrapyd/dbs/

ONBUILD ADD requirements.txt .
ONBUILD RUN pip --no-cache-dir install -r requirements.txt
ONBUILD RUN apk del ${BUILD_PACKAGES} && \
            rm -rf /root/.cache

COPY scrapyd.conf /etc/scrapyd/
COPY start.sh /etc/scrapyd/

EXPOSE 6800

CMD ["/bin/sh", "/etc/scrapyd/start.sh"]