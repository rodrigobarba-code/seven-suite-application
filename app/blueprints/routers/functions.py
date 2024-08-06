# Importing Necessary Libraries
import re
import ipaddress
from app.extensions import func
# Importing Necessary Libraries

# Importing Required Exceptions
from app.blueprints.routers.exceptions import *
# Importing Required Exceptions

# Class for Routers Functions
class RoutersFunctions:
    # Constructor
    def __init__(self):  # Constructor
        pass  # Pass the constructor
    # Constructor

    # Function to validate the Router IP
    @staticmethod
    def validate_ip(ip):
        try:
            ipaddress.ip_address(ip)  # Validate the IP Address
            return True  # Return True
        except ValueError:
            return False  # Return False
    # Function to validate the Router IP

    # Function to validate the Router MAC
    @staticmethod
    def validate_mac(mac):
        try:
            # Check if the MAC Address is correct
            if re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac.lower()):
                return True  # Return True
            else:
                return False  # Return False
        except ValueError:
            return False  # Return False
    # Function to validate the Router MAC
    
    # Function to validate the all the Router Details
    @staticmethod
    def validate_router(self, router, operation, model):
        try:
            if operation == "insert" or operation == "update":
                if operation == "update":
                    # Check if the router that will be updated exists
                    if not model.query.get(router.router_id):
                        # If the router does not exist, raise RouterNotFound Exception
                        raise RouterNotFound(
                            router.router_id  # Router ID
                        )
                    else:
                        # Check if the router name already exists
                        if model.query.filter(func.lower(model.router_name) == func.lower(router.router_name)).first():
                            # Raise RouterAlreadyExists Exception
                            raise RouterAlreadyExists(
                                router_id=model.query.filter(
                                    func.lower(model.router_name) == func.lower(router.router_name)).first().router_id,
                                router_name=router.router_name
                            )
                        else:
                            # Check if the router IP is valid
                            if not self.validate_ip(router.router_ip):
                                raise RouterIPNotValid(router.router_ip)  # Raise RouterIPNotValid Exception
                            # Check if the router MAC is valid
                            elif not self.validate_mac(router.router_mac):
                                raise RouterMACNotValid(router.router_mac)  # Raise RouterMACNotValid Exception
                            else:
                                # Check if the router IP is already in use
                                if model.query.filter(func.lower(model.router_ip) == func.lower(router.router_ip)).first():
                                    # Raise RouterIPAlreadyExists Exception
                                    raise RouterIPAlreadyExists(
                                        # Router ID
                                        router_id=model.query.filter(
                                            func.lower(model.router_ip) == func.lower(router.router_ip)).first().router_id,
                                        # Router IP
                                        router_ip=router.router_ip
                                    )
                                # Check if the router MAC is already in use
                                elif model.query.filter(
                                        func.lower(model.router_mac) == func.lower(router.router_mac)).first():
                                    # Raise RouterMACAlreadyExists Exception
                                    raise RouterMACAlreadyExists(
                                        # Router ID
                                        router_id=model.query.filter(
                                            func.lower(model.router_mac) == func.lower(router.router_mac)).first().router_id,
                                        # Router MAC
                                        router_mac=router.router_mac
                                    )
                                else:
                                    return True  # Return True
            elif operation == "delete" or operation == "get":
                # Check if the router exists
                if not model.query.filter(model.router_id == router.router_id).first():
                    # Raise RouterDoesNotExists Exception
                    raise RouterNotFound(router.router_id)  # Raise RouterNotFound Exception
                else:
                    return True  # Return True
        except (
                RouterNotFound,  # Router Not Found
                RouterIPNotValid,  # Router IP Not Valid
                RouterMACNotValid,  # Router MAC Not Valid
                RouterAlreadyExists,  # Router Already Exists
                RouterIPAlreadyExists,  # Router IP Already Exists
                RouterMACAlreadyExists  # Router MAC Already Exists
        ) as e:  # If any of the above exceptions occur
            raise e  # Raise the exception
        except Exception as e:  # If any other exception occurs
            raise RouterError()  # Raise RouterError Exception
    # Function to validate the all the Router Details
# Class for Routers Functions
