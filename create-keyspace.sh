#!/bin/bash
DDL_commands="
	CREATE KEYSPACE hw2_myntiuk WITH REPLICATION = {'class' : 'SimpleStrategy', 'replication_factor' : 1 };
	USE hw2_myntiuk;
	CREATE TABLE favorite_songs ( id int, author text, song_name text, release_year int, PRIMARY KEY (id));
	CREATE TABLE favorite_movies ( id int, name text, producer text, release_year int, PRIMARY KEY (id));
	DESCRIBE TABLES"

docker exec -it node1 cqlsh -e "${DDL_commands}"

