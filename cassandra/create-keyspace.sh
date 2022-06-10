#!/bin/bash
docker cp create-keyspace.cql cassandra-node:./create-keyspace.cql
docker exec -it cassandra-node cqlsh -f ./create-keyspace.cql

