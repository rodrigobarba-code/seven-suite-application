from .entities.session_information import SessionInformation

class ModelSessionInformation:

    @classmethod
    def add_session_information(self, db, session_information):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_add_session_information(%s, %s, %s, %s, %s, %s, %s, %s)", (
                session_information.session_ip_address,
                session_information.session_mac_address,
                session_information.session_username,
                session_information.session_password,
                session_information.session_connection_type,
                session_information.session_brand,
                session_information.session_model,
                session_information.allow_remote_access
            ))
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_session_information(self, db, session_information):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_update_session_information(%s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                session_information.session_id,
                session_information.session_ip_address,
                session_information.session_mac_address,
                session_information.session_username,
                session_information.session_password,
                session_information.session_connection_type,
                session_information.session_brand,
                session_information.session_model,
                session_information.allow_remote_access
            ))
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def delete_session_information(self, db, session_id):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_delete_session_information(%s)", (session_id,))
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_session_information_by_id(self, db, session_id):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_get_session_information_by_id(%s)", (session_id,))
            session = cursor.fetchone()
            cursor.close()
            return SessionInformation(
                session[0],
                session[1],
                session[2],
                session[3],
                session[4],
                session[5],
                session[6],
                session[7],
                session[8]
            )
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_all_session_information(self, db):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_get_all_session_information()")
            sessions = cursor.fetchall()
            cursor.close()
            return sessions
        except Exception as ex:
            raise Exception(ex)
