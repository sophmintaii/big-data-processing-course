#!/bin/bash
docker build -t write_kafka:1.0 .
docker run --rm --network kafka-network --rm write_kafka:1.0 --name write_kafka:1.0

