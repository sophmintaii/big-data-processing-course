#!/bin/bash

docker build . -t hw4_myntiuk:1.0
docker run --network  hw4_cassandra_python --rm hw4_myntiuk:1.0
