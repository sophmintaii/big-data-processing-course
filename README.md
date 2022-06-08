```
docker-compose up -d
```
```
docker ps
```
![image](https://user-images.githubusercontent.com/54286666/172711961-5ebea0a4-7439-4d48-887b-3f8718fc675c.png)

```
sh create-topic.sh
```

```
docker run -it --rm --network kafka-network -e KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper-server:2181 bitnami/kafka:latest kafka-topics.sh --list  --bootstrap-server kafka-server:9092
```
![image](https://user-images.githubusercontent.com/54286666/172712109-db6dff3d-0aea-4d55-a0b8-ec922c9a5378.png)

Launch consumer:
```
sh start-consumer.sh
```

In new terminal window launch producer:
```
sh start-producer.sh
```

Messages are sent from producer:
![image](https://user-images.githubusercontent.com/54286666/172712413-873821c4-f739-4908-9745-ad0677e4fd51.png)

Messages are received by consumer:
![image](https://user-images.githubusercontent.com/54286666/172712538-f371b52a-01b7-4d6a-9bdb-d6c8f738483e.png)


```
docker-compose down -d
```
