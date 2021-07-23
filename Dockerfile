FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY ./pakt_blog /app

RUN pip install -r app/requirements.txt