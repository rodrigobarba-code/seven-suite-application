# Importing Necessary Libraries
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import func
import requests as r
import socket
# Importing Necessary Libraries

# Importing Necessary Entities
from app.blueprints.users.entities import UserLogEntity
# Importing Necessary Entities

# Importing Necessary Models
from app.blueprints.users.models import UserLog
# Importing Necessary Models

# Creating Instances of SQLAlchemy and Migrate
func = func
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

# Create Record User Log Function
def create_record_user_log(
    user_log_id: int,  # User log ID
    fk_user_id: int,  # User ID
    user_log_description: str,  # Description
    user_log_action: str,  # Action
    user_log_table: str,  # Table
    user_log_date: str,  # Date
    user_log_public_ip: str,  # Public IP
    user_log_local_ip: str  # Local IP
):
    # Create a UserLogEntity object
    user_log = UserLogEntity(
        user_log_id=user_log_id,  # Set the log ID
        fk_user_id=fk_user_id,  # Set the user ID
        user_log_description=user_log_description,  # Set the description
        user_log_action=user_log_action,  # Set the action
        user_log_table=user_log_table,  # Set the table
        user_log_date=user_log_date,  # Set the date
        user_log_public_ip=user_log_public_ip,  # Set the public IP
        user_log_local_ip=user_log_local_ip  # Set the local IP
    )
    user_log.validate()  # Validate the user log
    UserLog.add_user_log(user_log)  # Add the user log to the database
# Create Record User Log Function
