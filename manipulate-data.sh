#!/bin/bash
DML_commands="
	USE hw2_myntiuk;
	INSERT INTO favorite_songs ( id, author, song_name, release_year) VALUES (1, 'Mykhailo Verbytsky, Pavlo Chubynsky', 'Ukrainian National Anthem', 1863);
	INSERT INTO favorite_songs ( id, author, song_name, release_year) VALUES (2, 'Pink Floyd feat. Andriy Khlyvnyuk of Boombox', 'Hey Hey Rise Up', 2022);
	INSERT INTO favorite_movies ( id, name, producer, release_year) VALUES (1, 'Little Women', 'Greta Gerwig', 2019);
	INSERT INTO favorite_movies ( id, name, producer, release_year) VALUES (2, 'Pride & Prejudice', 'Joe Wright', 2006);"
docker exec -it node1 cqlsh -e "${DML_commands}"
