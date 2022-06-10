import json

from flask import Flask

from read_from_cassandra import CassandraClient

app = Flask(__name__)
host = 'node1'
port = 9042

keyspace = 'hw4_myntiuk'


@app.get("/reviews_&product_id=<product_id>")
def get_reviews_by_product_id(product_id):
    res = json.dumps(client.select_product_reviews(product_id),
                     indent=4, sort_keys=True, default=str)
    return res


@app.get("/reviews_&product_id=<product_id>&star_rating=<int:star_rating>")
def get_reviews_by_product_id_star_rating(product_id, star_rating):
    res = json.dumps(client.select_product_reviews_star(product_id, star_rating),
                     indent=4, sort_keys=True, default=str)
    return res


@app.get("/reviews_&customer_id=<customer_id>")
def get_reviews_by_customer_id(customer_id):
    res = json.dumps(client.select_customer_reviews(customer_id),
                     indent=4, sort_keys=True, default=str)
    return res


@app.get("/most_reviewed_&num=<int:num>from=<date1>&to=<date2>")
def get_most_reviewed_products(num, date1, date2):
    res = json.dumps(client.select_most_rev(num, date1, date2),
                     indent=4, sort_keys=True, default=str)
    return res


@app.get("/most_active_users_&num=<int:num>from=<date1>&to=<date2>")
def get_most_active_users(num, date1, date2):
    res = json.dumps(client.select_most_prod(num, date1, date2),
                     indent=4, sort_keys=True, default=str)
    return res


@app.get("/most_active_haters_&num=<int:num>from=<date1>&to=<date2>")
def get_most_active_haters(num, date1, date2):
    res = json.dumps(client.select_most_prod_haters(num, date1, date2),
                     indent=4, sort_keys=True, default=str)
    return res


@app.get("/most_active_backers_&num=<int:num>from=<date1>&to=<date2>")
def get_most_active_backers(num, date1, date2):
    res = json.dumps(client.select_most_prod_backers(num, date1, date2),
                     indent=4, sort_keys=True, default=str)
    return res


if __name__ == '__main__':
    client = CassandraClient(host, port, keyspace)
    client.connect()
    app.run(host='0.0.0.0', port=8080)
