# Importing Necessary Libraries
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import requests as r
import socket
# Importing Necessary Libraries

# Creating Instances of SQLAlchemy and Migrate
db = SQLAlchemy()
migrate = Migrate()
# Creating Instances of SQLAlchemy and Migrate

# Get Public IP Address Function
def get_public_ip():
    endpoint = 'https://ipinfo.io/json'  # Endpoint to get the public IP address
    response = r.get(endpoint, verify=True)  # Send a GET request to the endpoint

    if response.status_code != 200:  # Check if the request was successful
        return 'Status:', response.status_code, 'Problem with the request. Exiting.'  # Return an error message

    data = response.json()  # Get the JSON data from the response
    return data['ip']  # Return the public IP address
# Get Public IP Address Function

# Get Local IP Address Function
def get_local_ip():
    return socket.gethostbyname(socket.gethostname())  # Return the local IP address
# Get Local IP Address Function
