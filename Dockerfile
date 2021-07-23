FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY ./src /app

RUN pip install -r /app/requirements.txt