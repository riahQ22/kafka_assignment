from kafka import KafkaConsumer
import json

#####def json_deserializer(data_product):
    ###############return json.loads(data_product).decode('utf-8')

consumer = KafkaConsumer("products", 
                         bootstrap_servers =['localhost:9092'],
                         auto_offset_reset='earliest',
                         group_id="consumer_group"
                        )
print('Starting the consumer')
for message in consumer:
##########message = message.value
    print(message.value)
#############print("Regist={}".format(json.loads(message)))