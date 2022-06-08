import csv

from datetime import datetime
from kafka import KafkaProducer
from json import dumps


producer = KafkaProducer(bootstrap_servers='kafka-server:9092', value_serializer=lambda x: dumps(x).encode('ascii'))

with open('twcs.csv', 'r') as f:
    tweets_file = csv.reader(f)
    header = next(tweets_file)
    for row in tweets_file:
        row[3] = datetime.now().strftime("%c")
        producer.send('tweets', row)
        producer.flush()
