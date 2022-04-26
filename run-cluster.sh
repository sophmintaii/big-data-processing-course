#!/bin/bash
docker network create hw2_cassandra_installation
docker run --rm --name node1 --network hw2_cassandra_installation -d cassandra:latest
docker run --rm --name node2 --network hw2_cassandra_installation -d -e CASSANDRA_SEEDS=node1 cassandra:latest
docker run --rm --name node3 --network hw2_cassandra_installation -d -e CASSANDRA_SEEDS=node1,node2 cassandra:latest
