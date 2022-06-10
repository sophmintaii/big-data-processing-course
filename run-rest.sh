#!/bin/bash
docker build . -t hw4_myntiuk
docker start node1
docker run --network  hw4_cassandra_python --rm hw4_myntiuk
