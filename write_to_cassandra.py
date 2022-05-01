import pandas as pd
from cassandra.cluster import Cluster


class CassandraClient:
    def __init__(self, host, port, keyspace):
        self.host = host
        self.port = port
        self.keyspace = keyspace
        self.session = None

    def connect(self):
        cluster = Cluster([self.host], port=self.port)
        self.session = cluster.connect(self.keyspace)

    def execute(self, query):
        self.session.execute(query)

    def close(self):
        self.session.shutdown()

    def insert_records(self, table, df):
        cols = ', '.join(df.columns)
        for _, row in df.iterrows():
            query = f"INSERT INTO {table} ({cols}) VALUES ({str([row[col] for col in df.columns])[1:-1]})"
            self.execute(query)

    def select_


if __name__ == '__main__':
    host = 'localhost'
    port = 9042
    keyspace = 'hw4_myntiuk'

    df = pd.read_csv('amazon_reviews_us_Books_v1_02.tsv', sep='\t', nrows=20)
    df['review_body'] = df['review_body'].str.replace(r"'", r"[\"]")
    df['product_title'] = df['product_title'].str.replace(r"'", r"[\"]")

    client = CassandraClient(host, port, keyspace)
    client.connect()

    client.insert_records(table='products', df=df[['customer_id', 'product_id', 'product_title', 'star_rating']])
    client.insert_records(table='reviews', df=df[['customer_id', 'review_id', 'product_id', 'product_title',
                                                 'star_rating', 'verified_purchase', 'review_body', 'review_date']])

    client.close()
