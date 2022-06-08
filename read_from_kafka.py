import csv
from kafka import KafkaConsumer
from json import loads


consumer = KafkaConsumer('tweets', bootstrap_servers= 'kafka-server:9092', 
                         value_deserializer=lambda x: loads(x.decode('ascii')))

previous_date = ''
tweets_lst = []
file_header = ['author_id', 'created_at', 'text']

for message in consumer:
    tweet = [message.value[1], message.value[3], message.value[4]]
    tweet_date = tweet[1]

    if not previous_date:
        previous_date = tweet_date

    if tweet_date != previous_date:
        with open(f'tweets_{previous_date}.csv', 'w') as f:
            write = csv.writer(f)
            write.writerow(file_header)
            write.writerows(tweets_lst)
        previous_date = tweet_date
        tweets_lst = [tweet]
        continue

    tweets_lst.append(tweet)
