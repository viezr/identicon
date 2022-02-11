FROM python:3.10.2-alpine3.15

RUN addgroup -S gunicorn && adduser -S gunicorn -G gunicorn

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install --upgrade pip \
    && pip install Flask==2.0.2 gunicorn==20.1.0 Pillow==9.0.1 \
    && apk del build-deps

WORKDIR /app
COPY app /app
COPY docker_cmd.sh /

EXPOSE 9090
USER gunicorn

CMD ["/docker_cmd.sh"]
