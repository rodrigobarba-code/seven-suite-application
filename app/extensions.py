# Importing Necessary Libraries
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import requests as r
import json as j
import socket
# Importing Necessary Libraries

# Creating Instances of SQLAlchemy and Migrate
db = SQLAlchemy()
migrate = Migrate()
# Creating Instances of SQLAlchemy and Migrate

# Get Public IP Address Function
def get_public_ip():
    endpoint = 'https://ipinfo.io/json'
    response = r.get(endpoint, verify=True)

    if response.status_code != 200:
        return 'Status:', response.status_code, 'Problem with the request. Exiting.'

    data = response.json()
    return data['ip']
# Get Public IP Address Function

# Get Local IP Address Function
def get_local_ip():
    return socket.gethostbyname(socket.gethostname())
# Get Local IP Address Function
