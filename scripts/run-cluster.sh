#!/bin/bash
docker network create hw4_cassandra_python
docker run --rm --name node1 --network hw4_cassandra_python -p 9042:9042 -d cassandra:latest
