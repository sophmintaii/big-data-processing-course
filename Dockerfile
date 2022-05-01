FROM python:3.9-slim

RUN apt-get update

RUN pip install --upgrade pip

RUN pip install cassandra-driver

RUN pip install Flask

COPY ./read_from_cassandra.py /opt/app/

COPY ./app.py /opt/app

ENV FLASK_APP /opt/app/app.py

ENTRYPOINT ["flask", "run"]
