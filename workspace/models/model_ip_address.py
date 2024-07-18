from .entities.ip_address import IPAddress
from .errors import Errors


class ModelIPAddress:

    # Add IP Address
    @classmethod
    def add_ip_address(cls, db, ip_address):
        try:
            # Create a cursor object using the cursor() method
            cursor = db.connection.cursor()
            # Execute the SQL procedure
            cursor.execute("CALL sp_add_ip_address(%s, %s, %s, %s, %s, %s, %s)", (
                ip_address.fk_router_id,
                ip_address.address_alias,
                ip_address.address_state,
                ip_address.address_ip,
                ip_address.address_netmask,
                ip_address.address_interface,
                ip_address.address_network,
            ))
            # Commit your changes in the database
            db.connection.commit()
            # Close the cursor
            cursor.close()
        except Exception as ex:
            raise Exception(ex)
    # Add IP Address

    # Update IP Address
    @classmethod
    def update_ip_address(cls, db, ip_address):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_update_ip_address(%s, %s, %s, %s, %s, %s, %s, %s)", (
                ip_address.address_id,
                ip_address.fk_router_id,
                ip_address.address_alias,
                ip_address.address_state,
                ip_address.address_ip,
                ip_address.address_netmask,
                ip_address.address_interface,
                ip_address.address_network,
            ))
            db.connection.commit()
            cursor.close()
        except Exception as ex:
            if '45012' in str(ex):
                raise Exception("Error: {error_number}, {error_message}".format(
                    error_number=Errors.errors['45012'][0],
                    error_message=Errors.errors['45012'][1]
                ))
            else:
                raise Exception(ex)
    # Update IP Address

    # Delete IP Address
    @classmethod
    def delete_ip_address(cls, db, ip_address):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_delete_ip_address(%s)", (
                ip_address.address_id,
            ))
            db.connection.commit()
            cursor.close()
        except Exception as ex:
            if '45012' in str(ex):
                raise Exception("Error: {error_number}, {error_message}".format(
                    error_number=Errors.errors['45012'][0],
                    error_message=Errors.errors['45012'][1]
                ))
            else:
                raise Exception(ex)
    # Delete IP Address
