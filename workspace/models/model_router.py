from .entities.router import Router
from .errors import Errors


class ModelRouter:

    # Add Router
    @classmethod
    def add_router(cls, db, router):
        try:
            # Create a cursor object using the cursor() method
            cursor = db.connection.cursor()
            # Execute the SQL procedure
            cursor.execute("CALL sp_add_router(%s, %s, %s, %s, %s)", (
                router.router_name,
                router.router_description,
                router.fk_site_id,
                router.router_brand,
                router.router_model
            ))
            # Commit your changes in the database
            db.connection.commit()
            # Close the cursor
            cursor.close()
        except Exception as ex:
            if '45010' in str(ex):
                raise Exception("Error: {error_number}, {error_message}".format(
                    error_number=Errors.errors['45010'][0],
                    error_message=Errors.errors['45010'][1]
                ))
            elif '45015' in str(ex):
                raise Exception("Error: {error_number}, {error_message}".format(
                    error_number=Errors.errors['45015'][0],
                    error_message=Errors.errors['45015'][1]
                ))
            else:
                raise Exception(ex)
    # Add Router

    # Update Router
    @classmethod
    def update_router(cls, db, router):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_update_router(%s, %s, %s, %s)", (
                router.router_id,
                router.router_name,
                router.router_description,
                router.fk_site_id
            ))
            db.connection.commit()
            cursor.close()
        except Exception as ex:
            if '45011' in str(ex):
                raise Exception("Error: {error_number}, {error_message}".format(
                    error_number=Errors.errors['45011'][0],
                    error_message=Errors.errors['45011'][1]
                ))
            elif '45010' in str(ex):
                raise Exception("Error: {error_number}, {error_message}".format(
                    error_number=Errors.errors['45010'][0],
                    error_message=Errors.errors['45010'][1]
                ))
            else:
                raise Exception(ex)
    # Update Router

    # Delete Router
    @classmethod
    def delete_router(cls, db, router):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_delete_router(%s)", (
                router.router_id,
            ))
            db.connection.commit()
            cursor.close()
        except Exception as ex:
            if '45012' in str(ex):
                raise Exception("Error: {error_number}, {error_message}".format(
                    error_number=Errors.errors['45012'][0],
                    error_message=Errors.errors['45012'][1]
                ))
            elif '45013' in str(ex):
                raise Exception("Error: {error_number}, {error_message}".format(
                    error_number=Errors.errors['45013'][0],
                    error_message=Errors.errors['45013'][1]
                ))
            else:
                raise Exception(ex)
    # Delete Router

    # Get Router
    @classmethod
    def get_router(cls, db, router_id):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_get_router(%s)", (
                router_id,
            ))
            router = cursor.fetchone()
            cursor.close()
            return Router(
                router_id=router[0],
                router_name=router[1],
                router_description=router[2],
                fk_site_id=router[3],
                fk_session_id=router[4]
            )
        except Exception as ex:
            if '45012' in str(ex):
                raise Exception("Error: {error_number}, {error_message}".format(
                    error_number=Errors.errors['45012'][0],
                    error_message=Errors.errors['45012'][1]
                ))
            else:
                raise Exception(ex)
    # Get Router

    # Get Routers
    @classmethod
    def get_routers(cls, db):
        try:
            router_list = []
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_get_routers()")
            routers = cursor.fetchall()
            for router in routers:
                router_list.append(Router(
                    router_id=router[0],
                    router_name=router[1],
                    router_description=router[2],
                    router_brand=router[3],
                    router_model=router[4],
                    fk_site_id=router[5],
                    fk_session_id=router[6]
                ))
            cursor.close()
            return router_list
        except Exception as ex:
            raise Exception(ex)
    # Get Routers
