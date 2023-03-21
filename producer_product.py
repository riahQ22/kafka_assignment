from kafka import KafkaProducer
import json
from data_product import get_product
import time

############def json_serializer(data_product):
    ###########return json.dumps(data_product).encode('utf-8')

producer =KafkaProducer(bootstrap_servers= ['localhost:9092'])


##########print(get_product)
producer.send("products", get_product)
time.sleep(3)
producer.flush()