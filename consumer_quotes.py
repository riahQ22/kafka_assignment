from kafka import KafkaConsumer
import json

#####def json_deserializer(data_product):
    ###############return json.loads(data_product).decode('utf-8')

consumer = KafkaConsumer("QuotesTopic", 
                         bootstrap_servers =['localhost:9092'],
                         auto_offset_reset='earliest',
                         group_id="consumer_group_quotes"
                        )
print('Starting the consumer')
for message in consumer:
    print(message.value)
