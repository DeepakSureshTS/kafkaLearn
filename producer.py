import json
import os
import socket
from time import sleep
from json import dumps
from kafka import KafkaProducer

from config import FORMAT, HOST, PORT,bootstrap_servers,topic_name



socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
       
socket_connection.connect((HOST,PORT))


producer = KafkaProducer(bootstrap_servers=bootstrap_servers, retries = 5,
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

while True:
    try :
            data=socket_connection.recv(1024).decode(FORMAT)
            json_acceptable_string = data.replace("'", "\"")
            load_data = json.loads(json_acceptable_string)
            print(load_data)
            for data in load_data:
                producer.send(topic_name,value=data)
             
    except Exception as exception:
            print(exception)

socket_connection.close()




