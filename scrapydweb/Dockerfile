FROM python:3.7.4-alpine3.10
MAINTAINER SHI TAO <shitao0418@gamil.com>

ENV LIBRARY_PATH=/lib:/usr/lib

ENV RUNTIME_PACKAGES ca-certificates libxslt libxml2 libpq
ENV BUILD_PACKAGES build-base libxslt-dev libxml2-dev libffi-dev openssl-dev postgresql-dev

WORKDIR /opt/

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories && \
    apk update && \
    apk upgrade && \
    apk add --no-cache --update ${RUNTIME_PACKAGES} ${BUILD_PACKAGES} && \
    apk add --no-cache --update git && \
    pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && \
    pip3 --no-cache-dir install -U pip scrapydweb && \
    rm -rf /root/.cache

ADD localtime /etc/localtime
ADD timezone /etc/timezone
ONBUILD ADD scrapydweb_settings_v10.py /opt/

EXPOSE 8001

CMD ["scrapydweb"]