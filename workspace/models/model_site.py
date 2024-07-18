from .entities.site import Site
from .errors import Errors


class ModelSite:

    # Add Site
    @classmethod
    def add_site(cls, db, site):
        try:
            # Create a cursor object using the cursor() method
            cursor = db.connection.cursor()
            # Execute the SQL procedure
            cursor.execute("CALL sp_add_site(%s, %s, %s)", (
                site.fk_region_id,
                site.site_name,
                site.site_segment
            ))
            # Commit your changes in the database
            db.connection.commit()
            # Close the cursor
            cursor.close()
        except Exception as ex:
            if '45004' in str(ex):
                raise Exception("Error: {error_number}, {error_message}".format(
                    error_number=Errors.errors['45004'][0],
                    error_message=Errors.errors['45004'][1]
                ))
            else:
                raise Exception(ex)
    # Add Site

    # Update Site
    @classmethod
    def update_site(cls, db, site):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_update_site(%s, %s, %s, %s)", (
                site.site_id,
                site.fk_region_id,
                site.site_name,
                site.site_segment
            ))
            db.connection.commit()
            cursor.close()
        except Exception as ex:
            if '45004' in str(ex):
                raise Exception("Error: {error_number}, {error_message}".format(
                    error_number=Errors.errors['45004'][0],
                    error_message=Errors.errors['45004'][1]
                ))
            elif '45005' in str(ex):
                raise Exception("Error: {error_number}, {error_message}".format(
                    error_number=Errors.errors['45005'][0],
                    error_message=Errors.errors['45005'][1]
                ))
            else:
                raise Exception(ex)
    # Update Site

    # Delete Site
    @classmethod
    def delete_site(cls, db, site_id):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_delete_site(%s)", (
                site_id,
            ))
            db.connection.commit()
            cursor.close()
        except Exception as ex:
            if '45005' in str(ex):
                raise Exception("Error: {error_number}, {error_message}".format(
                    error_number=Errors.errors['45005'][0],
                    error_message=Errors.errors['45005'][1]
                ))
            else:
                raise Exception(ex)
    # Delete Site

    # Get Site
    @classmethod
    def get_site(cls, db, site_id):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_get_site(%s)", (
                site_id,
            ))
            result = cursor.fetchone()
            site = Site(
                result[0],
                result[1],
                result[2],
                result[3]
            )
            cursor.close()
            return site
        except Exception as ex:
            if '45005' in str(ex):
                raise Exception("Error: {error_number}, {error_message}".format(
                    error_number=Errors.errors['45005'][0],
                    error_message=Errors.errors['45005'][1]
                ))
            else:
                raise Exception(ex)
    # Get Site

    # Get Sites
    @classmethod
    def get_sites(cls, db):
        try:
            sites_list = []
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_get_sites")
            sites = cursor.fetchall()
            for i in range(len(sites)):
                sites_list.append(Site(
                    sites[i][0],
                    sites[i][1],
                    sites[i][2],
                    sites[i][3]
                ))
            cursor.close()
            return sites_list
        except Exception as ex:
            raise Exception(ex)
    # Get Sites

    # Get Region Name
    @classmethod
    def get_region_name(cls, db, site_name):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_get_region_name(%s)", (
                site_name,
            ))
            result = cursor.fetchone()
            cursor.close()
            return result[0]
        except Exception as ex:
            if '45005' in str(ex):
                raise Exception("Error: {error_number}, {error_message}".format(
                    error_number=Errors.errors['45005'][0],
                    error_message=Errors.errors['45005'][1]
                ))
            else:
                raise Exception(ex)
    # Get Region Name
