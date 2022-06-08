twcs.csv should be in this folder.

```
docker-compose up -d
```
Launch consumer:
```
sh start-consumer.sh
```
In the new terminal window launch producer:
```
sh start-producer-app.sh
```
```
docker ps
```
![image](https://user-images.githubusercontent.com/54286666/172720143-48dad7ca-4f0f-4f56-a8cd-d579779882db.png)

After few minutes of running check created files
```
ls tweets*.csv
```
![image](https://user-images.githubusercontent.com/54286666/172721567-1a482816-7325-4ed0-b641-f12721dcce74.png)


Files examples:
![image](https://user-images.githubusercontent.com/54286666/172721793-78c9e373-e44a-4cea-b6c7-7c71fdbc34ca.png)

![image](https://user-images.githubusercontent.com/54286666/172721863-ea3ab443-6d81-4d22-8aac-13919010a65a.png)

```
docker-compose down
```
