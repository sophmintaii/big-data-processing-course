#!/bin/sh
docker stop kafka-server zookeeper-server
docker rm kafka-server zookeeper-server
docker network rm kafka-network