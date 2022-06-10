#!/bin/bash
docker run --name cassandra-node --network kafka-network -d cassandra:latest 

