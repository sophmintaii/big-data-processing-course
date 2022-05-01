# Homework 4: Cassandra interaction through python code

## Instructions on running:

Clone the repository
```bash
git clone git@github.com:sophmintaii/big-data-processing-course.git
cd big-data-processing-course
git checkout hw4-cassandra-interaction-python
```

Make sure you are in the project directory before running the following commands.

1. Running the cluster
```bash
bash scripts/run-sluster.sh
```

2. Creating the keyspace with DDL commands
```bash
bash scripts/create-keyspace.sh
```

3. Write the data from the .tsv file to the database.
Make sure that the .tsv file is in the same directory.
```bash
bash scripts/write-data.sh
```
You should get an output like this:

![shutdown-cluster.sh results](screenshots/write-data-results.png)

4. Building a Docker container
```bash
bash scripts/run-rest.sh
```

5. 