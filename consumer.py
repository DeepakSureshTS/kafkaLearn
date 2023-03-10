import json

from mongoengine import connect
from kafka import KafkaConsumer
from pydantic import BaseModel
import sys

import models

connect(db="SCM", host= "localhost")
bootstrap_servers = ['localhost:9092']
topicName = 'device_data'


try:
    consumer = KafkaConsumer(topicName,bootstrap_servers = bootstrap_servers,auto_offset_reset = 'earliest')
    for data in consumer:
        data = json.loads(data.value)
        Transport_Data = models.DeviceData(
            Battery_Level = data['Battery_Level'],
            Device_Id = data['Device_Id'],
            First_Sensor_temperature = data['First_Sensor_temperature'],
            Route_From = data['Route_From'],
            Route_To = data['Route_To']                        
        )
        
        Transport_Data.save() 
        print(Transport_Data)
except KeyboardInterrupt:
    sys.exit()