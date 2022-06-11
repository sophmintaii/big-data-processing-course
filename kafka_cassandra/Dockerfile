FROM python:3.9-slim

RUN apt-get update

RUN pip install --upgrade pip
RUN pip install kafka-python
RUN pip install cassandra-driver

COPY ./from_kafka.py .

CMD [ "python3", "from_kafka.py"]
