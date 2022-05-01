from cassandra.cluster import Cluster
from cassandra.query import dict_factory


class CassandraClient:
    def __init__(self, host, port, keyspace):
        self.host = host
        self.port = port
        self.keyspace = keyspace
        self.session = None

    def connect(self):
        cluster = Cluster([self.host], port=self.port)
        self.session = cluster.connect(self.keyspace)
        self.session.row_factory = dict_factory

    def execute(self, query):
        self.session.execute(query)

    def close(self):
        self.session.shutdown()

    def read_from_table(self, table_name):
        query = "SELECT * FROM %s" % table_name
        rows = self.session.execute(query)
        for row in rows:
            print(row)

    def select_product_reviews(self, product_id):
        # query = f"SELECT review_body FROM products WHERE product_id = '{product_id}';"
        query = f"SELECT * FROM products;"
        print(query)
        return list(self.session.execute(query))

    def select_product_reviews_star(self, product_id, star_rating):
        query = f"SELECT review_body FROM products WHERE product_id = '{product_id}' AND star_rating = {star_rating};"
        return list(self.session.execute(query))

    def select_customer_reviews(self, customer_id):
        query = f"SELECT review_body FROM reviews WHERE customer_id = {customer_id};"
        return list(self.session.execute(query))

if __name__ == '__main__':
    host = 'localhost'
    port = 9042
    keyspace = 'hw4_myntiuk'

    client = CassandraClient(host, port, keyspace)
    client.connect()

    print(client.select_product_reviews('015602943X'))
    print(client.select_product_reviews_star('015602943X', 5))
    print(client.select_customer_reviews(30501489))

    client.close()