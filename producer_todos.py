from kafka import KafkaProducer
import json
from data_todos import get_todos
import time

def json_serializer(data_todos):
    return json.dumps(data_todos).encode('utf-8')

producer =KafkaProducer(bootstrap_servers= ['localhost:9092'],
                        value_serializer = json_serializer)

producer.send("todos_topic", get_todos)
time.sleep(3)
producer.flush()



