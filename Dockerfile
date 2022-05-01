FROM python:3.9-slim

RUN apt-get update

RUN pip install --upgrade pip

RUN pip install cassandra-driver

COPY ./read_from_cassandra.py /opt/app/

ENTRYPOINT ["python", "/opt/app/read_from_cassandra.py"]
