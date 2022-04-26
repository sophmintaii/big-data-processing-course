#!/bin/bash
docker exec -it node1 cqlsh -e "SELECT * FROM hw2_myntiuk.favorite_songs;"
docker exec -it node1 cqlsh -e "SELECT * FROM hw2_myntiuk.favorite_movies;"
