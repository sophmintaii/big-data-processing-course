#!/bin/bash
docker build -f ./Dockerfile.rest . -t write_cassandra:1.0
docker run --network kafka-network --rm write_cassandra:1.0

