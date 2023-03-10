import os
import socket
from dotenv import load_dotenv


load_dotenv()

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050         
bootstrap_servers=['localhost:9092']

FORMAT = 'utf-8'
topic_name= "devicedata"