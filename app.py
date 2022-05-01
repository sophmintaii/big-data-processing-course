import json
from flask import Flask, request, jsonify
from read_from_cassandra import CassandraClient

app = Flask(__name__)
host = 'localhost'

port = 9042
keyspace = 'hw4_myntiuk'

@app.get("/reviews_product_id/<product_id>")
def get_reviews_by_product_id(product_id):
    return json.dumps(client.select_product_reviews(product_id))

@app.get("/reviews_product_id_star_rating/<product_id>/<star_rating>")
def get_reviews_by_product_id_star_rating(product_id, star_rating):
    return json.dumps(client.select_product_reviews_star(product_id, star_rating))

@app.get("/reviews_customer_id/<customer_id>")
def get_reviews_by_customer_id(customer_id):
    return json.dumps(client.select_customer_reviews(customer_id))

if __name__ == "__main__":
    client = CassandraClient(host, port, keyspace)
    client.connect()
    app.run(host=host, port=8080)
