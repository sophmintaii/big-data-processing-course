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
bash run-sluster.sh
```

2. Creating the keyspace with DDL commands
```bash
bash create-keyspace.sh
```

3. Write the data from the .tsv file to the database.
Make sure that the .tsv file is in the same directory.
```bash
python3 write_to_cassandra.py
```
You should get an output like this:

![shutdown-cluster.sh results](screenshots/write-data-results.png)

4. Building a Docker container
```bash
bash run-rest.sh
```

5. Using the app to select data (examples)
(the scripts were run not on all of the dataset as data writing takes quite a lot of time, sorry :( )

![image](https://user-images.githubusercontent.com/54286666/173142165-375768e0-6943-4d78-bf3c-268af7586f3e.png)

![image](https://user-images.githubusercontent.com/54286666/173142549-40772b5f-e046-40a8-852d-45461b87e709.png)

![image](https://user-images.githubusercontent.com/54286666/173142690-6232d31f-b63c-4328-8483-8ef6fbea1f9a.png)

![image](https://user-images.githubusercontent.com/54286666/173143787-09d3a230-817f-462c-98a2-5060c4aed594.png)

![image](https://user-images.githubusercontent.com/54286666/173143884-8447cec2-5aa0-43d5-ab4c-c474ce88dd57.png)

![image](https://user-images.githubusercontent.com/54286666/173143972-5d859887-8df6-49a3-8b26-68aad0598c57.png)

![image](https://user-images.githubusercontent.com/54286666/173144091-b38e375f-b4d0-4725-9ca5-ef2dcb2a1d60.png)

