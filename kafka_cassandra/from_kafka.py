from json import loads

from cassandra.query import dict_factory
from kafka import KafkaConsumer

consumer = KafkaConsumer('kafka-topic',
                         bootstrap_servers=['kafka-server:9092'],
                         value_deserializer=lambda x:
                         loads(x.decode('ascii')))


class CassandraClient:
    def __init__(self, host, port, keyspace):
        self.host = host
        self.port = port
        self.keyspace = keyspace
        self.session = None

    def connect(self):
        from cassandra.cluster import Cluster
        cluster = Cluster([self.host], port=self.port)
        self.session = cluster.connect(self.keyspace)
        self.session.row_factory = dict_factory

    def close(self):
        self.session.shutdown()

    def select_fraud_transactions(self, uid):
        query = f"SELECT * from uid_fraud WHERE nameOrig = '{uid}' AND isFraud = 1;"
        # query = f"SELECT * from uid_fraud WHERE nameOrig = '{uid}';"
        # query = f"SELECT * from uid_fraud;"
        return list(self.session.execute(query))

    def select_large_transactions(self, uid):
        query = f"SELECT * from uid_fraud WHERE nameOrig = '{uid}';"
        return sorted(list(self.session.execute(query)), reverse=True, key=lambda d: d['amount'])[:3]

    def select_received_transactions(self, uid, date1, date2):
        query = f"SELECT * FROM uid_date WHERE nameDest='{uid}' AND transactionDate < '{date2}'"\
                        f" AND transactionDate > '{date1}'"
        # query = f"SELECT * FROM uid_date;"

        res = list(self.session.execute(query))
        return sum([entry['amount'] for entry in res])
        # return list(self.session.execute(query))

    def insert_data(self, tables, row):
        for table in tables:
            query = f"INSERT INTO {table} (step, type, amount, nameOrig, oldbalanceOrg, newbalanceOrig, nameDest, " \
                    f"oldbalanceDest, newbalanceDest, isFraud, isFlaggedFraud, transactionDate) " \
                    f"VALUES ({row['step']}, '{row['type']}', {row['amount']}, '{row['nameOrig']}', "\
                    f"{row['oldbalanceOrg']},  {row['newbalanceOrig']}, '{row['nameDest']}', {row['oldbalanceDest']},"\
                    f" {row['newbalanceDest']}, {row['isFraud']}, {row['isFlaggedFraud']}, '{row['transactionDate']}')"
            # print(query)
            self.session.execute(query)


def main():
    # print('connected to the consumer')
    client = CassandraClient(host='cassandra-node', port=9042, keyspace='hw8_myntiuk')
    client.connect()
    # print('connected to the client')

    k = 0
    for message in consumer:
        data = message.value
        if k < 10:
            print(data)
        client.insert_data(['uid_fraud', 'uid_date'], data)
        k += 1

    # print(client.select_fraud_transactions('C1305486145'))

    client.close()


if __name__ == '__main__':
    main()
