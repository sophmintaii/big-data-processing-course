import csv
import datetime
import random
from json import dumps

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='kafka-server:9092',
                         value_serializer=lambda x:
                         dumps(x).encode('ascii'))

if __name__ == '__main__':
    with open('PS_20174392719_1491204439457_log.csv', 'r') as file:
        # print('opened the file')
        reader = csv.reader(file)
        # print('reader initialized')
        header = next(reader)
        k = 0
        for line in reader:
            random_day = random.randrange(30)
            random_date = datetime.datetime.now() - datetime.timedelta(days=random_day)

            # new_row = {key: row[key] for key in ['type', 'amount', 'nameOrig', 'nameDest', 'isFraud']}
            row = dict(zip(header, line))
            row['transactionDate'] = random_date.strftime("%Y-%m-%d")
            if k < 10:
                print(row)

            producer.send('kafka-topic', row)
            producer.flush()
            k += 1
        # print(f'sent {k} lines')
