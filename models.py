
from mongoengine import Document, StringField, IntField, DateField, DynamicDocument

class DeviceData(DynamicDocument):
    Battery_Level = IntField()
    Device_Id = IntField()
    First_Sensor_temperature = IntField()
    Route_From = StringField()
    Route_To = StringField()  

