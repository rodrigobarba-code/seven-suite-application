from .entities.session_information import SessionInformation
from .errors import Errors


class ModelSessionInformation:

    # Add Session Information
    @classmethod
    def add_session_information(cls, db, session):
        try:
            # Create a cursor object using the cursor() method
            cursor = db.connection.cursor()
            # Execute the SQL procedure
            cursor.execute("CALL sp_add_session_information(%, %, %, %, %, %, %, %)", (
                session.session_ip,
                session.session_mac,
                session.session_username,
                session.session_password,
                session.session_via,
                session.api_port,
                session.api_ssl_port,
                session.allow_scan
            ))
            # Commit your changes in the database
            db.connection.commit()
            # Close the cursor
            cursor.close()
        except Exception as ex:
            if '45006' in str(ex):
                raise Exception("Error: {error_number}, {error_message}".format(
                    error_number=Errors.errors['45006'][0],
                    error_message=Errors.errors['45006'][1]
                ))
            elif '45007' in str(ex):
                raise Exception("Error: {error_number}, {error_message}".format(
                    error_number=Errors.errors['45007'][0],
                    error_message=Errors.errors['45007'][1]
                ))
            elif '45008' in str(ex):
                raise Exception("Error: {error_number}, {error_message}".format(
                    error_number=Errors.errors['45008'][0],
                    error_message=Errors.errors['45008'][1]
                ))
            else:
                raise Exception(ex)
    # Add Session

    # Update Session information
    @classmethod
    def update_session_information(cls, db, session):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_update_session_information(%s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                session.session_id,
                session.session_ip,
                session.session_mac,
                session.session_username,
                session.session_password,
                session.session_via,
                session.api_port,
                session.api_ssl_port,
                session.allow_scan
            ))
            db.connection.commit()
            cursor.close()
        except Exception as ex:
            if '45009' in str(ex):
                raise Exception("Error: {error_number}, {error_message}".format(
                    error_number=Errors.errors['45009'][0],
                    error_message=Errors.errors['45009'][1]
                ))
            else:
                raise Exception(ex)
    # Update Session information

    # Delete Session information
    @classmethod
    def delete_session_information(cls, db, session_id):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_delete_session_information(%s)", (
                session_id,
            ))
            db.connection.commit()
            cursor.close()
        except Exception as ex:
            if '45009' in str(ex):
                raise Exception("Error: {error_number}, {error_message}".format(
                    error_number=Errors.errors['45009'][0],
                    error_message=Errors.errors['45009'][1]
                ))
            else:
                raise Exception(ex)
    # Delete Session information

    # Get Session information
    @classmethod
    def get_session_information(cls, db, session_id):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_get_session_information(%s)", (
                session_id,
            ))
            result = cursor.fetchone()
            cursor.close()
            return SessionInformation(
                result[0],
                result[1],
                result[2],
                result[3],
                result[4],
                result[5],
                result[6],
                result[7],
                result[8]
            )
        except Exception as ex:
            if '45009' in str(ex):
                raise Exception("Error: {error_number}, {error_message}".format(
                    error_number=Errors.errors['45009'][0],
                    error_message=Errors.errors['45009'][1]
                ))
            else:
                raise Exception(ex)
    # Get Session information

    # Get Sessions information
    @classmethod
    def get_sessions_information(cls, db):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_get_sessions_information()")
            result = cursor.fetchall()
            cursor.close()
            sessions = []
            for session in result:
                sessions.append(SessionInformation(
                    session[0],
                    session[1],
                    session[2],
                    session[3],
                    session[4],
                    session[5],
                    session[6],
                    session[7],
                    session[8]
                ))
            return sessions
        except Exception as ex:
            raise Exception(ex)
    # Get Sessions information
