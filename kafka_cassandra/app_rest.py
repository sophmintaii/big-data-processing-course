import json

from flask import Flask

from from_kafka import CassandraClient

app = Flask(__name__)
host = 'cassandra-node'
port = 9042
keyspace = 'hw8_myntiuk'


@app.get("/fraud&uid=<uid>")
def get_fraud_transactions(uid):
    return json.dumps(client.select_fraud_transactions(uid), indent=4, sort_keys=True, default=str)


@app.get("/sum&uid=<uid>&date1=<date1>&date2=<date2>")
def get_transactions_by_date(uid, date1, date2):
    return json.dumps(client.select_received_transactions(uid, date1, date2), indent=4, sort_keys=True, default=str)


@app.get("/large&uid=<uid>")
def get_largest_transactions(uid):
    return json.dumps(client.select_large_transactions(uid), indent=4, sort_keys=True, default=str)


if __name__ == "__main__":
    client = CassandraClient(host, port, keyspace)
    client.connect()
    app.run(host='0.0.0.0', port=8080)
