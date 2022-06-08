twcs.csv should be in this folder.

```
docker-compose up -d
```
```
docker ps
```
![image](https://user-images.githubusercontent.com/54286666/172715304-20247d41-5a93-4c02-bc7d-599d11778b6e.png)


Launch consumer:
```
sh start-consumer.sh
```

In the new terminal window start sending tweets with python app:
```
sh start-producer-app.sh
```
![image](https://user-images.githubusercontent.com/54286666/172718806-a84bbed5-f46a-4653-bfb9-e002959d7152.png)

Messages are received by consumer:
![image](https://user-images.githubusercontent.com/54286666/172718486-5f0c0b83-3b66-4b50-9d7d-7733829ecc17.png)
(...)
![image](https://user-images.githubusercontent.com/54286666/172718637-bbd61ec0-4212-42a0-873a-823fc5830014.png)
(sorry i did not wait for all the messages to process:()

```
docker-compose down
```
