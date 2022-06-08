docker build . -t kafka_producer:1.0
docker run --network kafka-network --rm kafka_producer:1.0