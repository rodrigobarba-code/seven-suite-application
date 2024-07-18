from .entities.region import Region
from .errors import Errors


class ModelRegion:

    # Add Region
    @classmethod
    def add_region(cls, db, region):
        try:
            # Create a cursor object using the cursor() method
            cursor = db.connection.cursor()
            # Execute the SQL procedure
            cursor.execute("CALL sp_add_region(%s)", (
                region.region_name,
            ))
            # Commit your changes in the database
            db.connection.commit()
            # Close the cursor
            cursor.close()
        except Exception as ex:
            if '45001' in str(ex):
                raise Exception("Error: {error_number}, {error_message}".format(
                    error_number=Errors.errors['45001'][0],
                    error_message=Errors.errors['45001'][1]
                ))
            else:
                raise Exception(ex)
    # Add Region

    # Update Region
    @classmethod
    def update_region(cls, db, region):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_update_region(%s, %s)", (
                region.region_id,
                region.region_name
            ))
            db.connection.commit()
        except Exception as ex:
            if '45001' in str(ex):
                raise Exception("Error: {error_number}, {error_message}".format(
                    error_number=Errors.errors['45001'][0],
                    error_message=Errors.errors['45001'][1]
                ))
            elif '45002' in str(ex):
                raise Exception("Error: {error_number}, {error_message}".format(
                    error_number=Errors.errors['45002'][0],
                    error_message=Errors.errors['45002'][1]
                ))
            else:
                raise Exception(ex)
    # Update Region

    # Delete Region
    @classmethod
    def delete_region(cls, db, region_id):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_delete_region(%s)", (region_id,))
            db.connection.commit()
        except Exception as ex:
            if '45002' in str(ex):
                raise Exception("Error: {error_number}, {error_message}".format(
                    error_number=Errors.errors['45002'][0],
                    error_message=Errors.errors['45002'][1]
                ))
            elif '45003' in str(ex):
                raise Exception("Error: {error_number}, {error_message}".format(
                    error_number=Errors.errors['45003'][0],
                    error_message=Errors.errors['45003'][1]
                ))
            else:
                raise Exception(ex)
    # Delete Region

    # Get Regions
    @classmethod
    def get_regions(cls, db):
        try:
            regions_list = []
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_get_regions")
            regions = cursor.fetchall()
            for i in range(len(regions)):
                regions_list.append(Region(
                    regions[i][0],
                    regions[i][1]
                ))
            cursor.close()
            return regions_list
        except Exception as ex:
            raise Exception(ex)
    # Get Regions

    # Get Region
    @classmethod
    def get_region(cls, db, region_id):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_get_region(%s)", (region_id,))
            region = cursor.fetchone()
            cursor.close()
            return Region(
                region[0],
                region[1]
            )
        except Exception as ex:
            if '45002' in str(ex):
                raise Exception("Error: {error_number}, {error_message}".format(
                    error_number=Errors.errors['45002'][0],
                    error_message=Errors.errors['45002'][1]
                ))
            else:
                raise Exception(ex)
    # Get Region
