FROM python:3.9-slim

COPY ./main.py /opt/app/

ENTRYPOINT ["python3", "/opt/app/main.py"]
