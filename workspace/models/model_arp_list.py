from .entities.arp_list import ARPList
from .errors import Errors


class ModelARPList:

    # Add IP Address
    @classmethod
    def add_arp_list(cls, db, arp_list):
        try:
            # Create a cursor object using the cursor() method
            cursor = db.connection.cursor()
            # Execute the SQL procedure
            cursor.execute("CALL sp_add_arp_list(%s, %s, %s, %s, %s, %s)", (
                arp_list.fk_router_id,
                arp_list.arp_state,
                arp_list.arp_ip,
                arp_list.arp_mac,
                arp_list.arp_interface,
                arp_list.arp_netbios
            ))
            # Commit your changes in the database
            db.connection.commit()
            # Close the cursor
            cursor.close()
        except Exception as ex:
            raise Exception(ex)
    # Add ARP List

    # Delete ARP List
    @classmethod
    def delete_arp_list(cls, db, arp_list):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_delete_arp_list(%s)", (
                arp_list.arp_id,
            ))
            db.connection.commit()
            cursor.close()
        except Exception as ex:
            if '45014' in str(ex):
                raise Exception("Error: {error_number}, {error_message}".format(
                    error_number=Errors.errors['45014'][0],
                    error_message=Errors.errors['45014'][1]
                ))
            else:
                raise Exception(ex)
    # Delete ARP List