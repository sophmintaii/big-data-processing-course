#!/bin/sh
docker run -d --rm --network kafka-network -e KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper-server:2181 bitnami/kafka:latest kafka-topics.sh --create  --bootstrap-server kafka-server:9092 --replication-factor 1 --partitions 3 --topic tweets

docker build -f Dockerfile.read . -t kafka_consumer:1.0
docker run --network kafka-network -v ~/Documents/ucu/big-data-processing-course:/big-data-processing-course --rm kafka_consumer:1.0
