from .entities.user import User
from .errors import Errors


class ModelUsers:

    # Add User
    @classmethod
    def add_user(cls, db, user):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_add_user(%s, %s, %s, %s, %s, %s)", (
                user.username,
                user.password,
                user.name,
                user.password,
                user.lastname,
                user.privileges
            ))
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
    # Add User

    # Update User
    @classmethod
    def update_user(cls, db, user):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_update_user(%s, %s, %s, %s, %s, %s, %s)", (
                user.user_id,
                user.username,
                user.password,
                user.name,
                user.lastname,
                user.privileges
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
    # Update User

    # Delete User
    @classmethod
    def delete_user(cls, db, user_id):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_delete_user(%s)", (user_id,))
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
    # Delete User

    # Get User
    @classmethod
    def get_user(cls, db, user_id):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_get_user(%s)", (user_id,))
            user = cursor.fetchone()
            cursor.close()
            return User(user[0], user[1], user[2], user[3], user[4], user[5])
        except Exception as ex:
            if '45003' in str(ex):
                raise Exception("Error: {error_number}, {error_message}".format(
                    error_number=Errors.errors['45003'][0],
                    error_message=Errors.errors['45003'][1]
                ))
            else:
                raise Exception(ex)
    # Get User

    # Get Users
    @classmethod
    def get_users(cls, db):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_get_users()")
            users = cursor.fetchall()
            cursor.close()
            return users
        except Exception as ex:
            raise Exception(ex)
    # Get Users
