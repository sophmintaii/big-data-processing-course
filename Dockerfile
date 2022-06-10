FROM python:3.9-slim

RUN pip install --upgrade pip

RUN pip install cassandra-driver

RUN pip install Flask

COPY ./read_from_cassandra.py /opt/app/

COPY ./app_cass.py /opt/app

ENTRYPOINT ["python", "/opt/app/app_cass.py"]
