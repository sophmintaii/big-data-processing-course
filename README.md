# Homework 4: Cassandra interaction through python code

## Instructions on running:

Clone the repository
```bash
git clone git@github.com:sophmintaii/big-data-processing-course.git
cd big-data-processing-course
git checkout hw4-cassandra-interaction-python
```

Make sure you are in the project directory before running the following commands.

create Kafka cluster and topic:
![image](https://user-images.githubusercontent.com/54286666/173170444-5de8518d-d11e-413f-8b1d-08b51d315409.png)

create Cassandra cluster and run ```docker ps``` to check:
![image](https://user-images.githubusercontent.com/54286666/173170467-e7b18340-a77e-4b56-8d6b-1868988e4b71.png)

run the DLL script:
![image](https://user-images.githubusercontent.com/54286666/173170519-7b56a752-4e82-4295-9ba0-cbad5a66d50c.png)

start the script to receive messages:
![image](https://user-images.githubusercontent.com/54286666/173170543-6637bd80-b20a-4bd6-bcb9-1c17c1dba70b.png)

in a separate terminal, start the script to get data from the file and send messages:
![image](https://user-images.githubusercontent.com/54286666/173170570-257f04a5-086c-4e3b-9e46-62023bf89e29.png)

leave the system for a couple of minutes and drink coffee or smth

after coming back, you can stop the processes and see what did we send:
![image](https://user-images.githubusercontent.com/54286666/173170665-85c345b9-ebe2-4628-8b51-92bc31a3553d.png)

and what did we get:
![image](https://user-images.githubusercontent.com/54286666/173170689-3aa80984-e841-42ba-a130-13cc2b1416f6.png)

(only a few data entries are shown, but the general idea is pretty understandable)

now, we can start a rest api to try selecting the data:

![image](https://user-images.githubusercontent.com/54286666/173171027-5449a64f-9d94-4f81-8fbd-9ec42106f0b0.png)

![image](https://user-images.githubusercontent.com/54286666/173171000-4d436088-6256-449c-a19a-aeae4e5c8b4c.png)

![image](https://user-images.githubusercontent.com/54286666/173172241-262fe927-2d56-42ec-8a1f-eb18c97e5198.png)



