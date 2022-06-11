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
        return list(self.session.execute(query))

    def select_large_transactions(self, uid):
        query = f"SELECT * from uid_fraud WHERE nameOrig = '{uid}';"
        return sorted(list(self.session.execute(query)), reverse=True, key=lambda d: d['amount'])[:-3]

    def select_received_transactions(self, uid, date1, date2):
        query = f"SELECT SUM(amount) from uid_date WHERE nameDest = '{uid}' AND (transactionDate >= '{date1}') " \
                "AND (transactionDate <= '{date2}');"
        res = list(self.session.execute(query))
        return sum([entry['amount'] for entry in res])

    def insert_data(self, tables, row):
        str_row = ', '.join(list(row.values))
        for table in tables:
            query = f"INSERT INTO {table} (step, type, amount, nameOrig, oldbalanceOrg, newbalanceOrig, nameDest, " \
                    f"oldbalanceDest, newbalanceDest, isFraud, isFlaggedFraud, transactionDate) " \
                    f"VALUES ({str_row})"
            self.session.execute(query)


def main():
    client = CassandraClient(host='cassandra-node', port=9042, keyspace='hw8_myntiuk')
    client.connect()

    for message in consumer:
        data = message.value
        client.insert_data(['uid_fraud', 'uid_date'], data)

    client.close()


if __name__ == '__main__':
    main()
