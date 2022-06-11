#!/bin/bash
docker build -f ./Dockerfile.from_kafka . -t write_cassandra:1.0
docker run --rm --network kafka-network -v --rm write_cassandra:1.0

