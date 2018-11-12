FROM tiangolo/uwsgi-nginx-flask:python3.7

ENV STATIC_INDEX 1
ENV NGINX_WORKER_PROCESSES auto

COPY ./app /app
