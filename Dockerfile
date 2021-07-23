FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY ./pakt_blog /app

RUN pip install -r pakt_blog/requirements.txt