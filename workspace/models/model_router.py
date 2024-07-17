from .entities.router import Router
from .sql_errors import SQLErrors


class ModelRouter:

    # Add Router
    @classmethod
    def add_router(cls, db, router):
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
                    error_number=SQLErrors.errors['45004'][0],
                    error_message=SQLErrors.errors['45004'][1]
                ))
            else:
                raise Exception(ex)
    # Add Router
