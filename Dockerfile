FROM python:3.10.2-alpine3.15

RUN addgroup -S gunicorn && adduser -S gunicorn -G gunicorn

RUN pip install Flask==2.0.2 gunicorn==20.1.0
WORKDIR /app
COPY app /app
COPY docker_cmd.sh /

EXPOSE 9090
USER gunicorn

CMD ["/docker_cmd.sh"]
