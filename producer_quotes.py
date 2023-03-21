from kafka import KafkaProducer
import json
from data_quotes import get_quotes
import time

def json_serializer(data_quotes):
    return json.dumps(data_quotes).encode('utf-8')

producer =KafkaProducer(bootstrap_servers= ['localhost:9092'],
                        value_serializer = json_serializer)

producer.send("QuotesTopic", get_quotes)
time.sleep(3)
producer.flush()



