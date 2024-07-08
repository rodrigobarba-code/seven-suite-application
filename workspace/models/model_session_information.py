from .entities.session_information import SessionInformation

class ModelSessionInformation:

    @classmethod
    def add_session_information(self, db, session_information):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_add_session_information(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                session_information.fk_site_id,
                session_information.fk_user_id,
                session_information.session_start,
                session_information.session_end,
                session_information.session_duration,
                session_information.session_status,
                session_information.session_notes,
                session_information.session_type,
                session_information.session_location,
                session_information.session_region,
                session_information.session_country
            ))
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_session_information(self, db, session_information):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_update_session_information(% s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s)", (
                session_information.session_id,
                session_information.fk_site_id,
                session_information.fk_user_id,
                session_information.session_start,
                session_information.session_end,
                session_information.session_duration,
                session_information.session_status,
                session_information.session_notes,
                session_information.session_type,
                session_information.session_location,
                session_information.session_region,
                session_information.session_country
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
                session[8],
                session[9],
                session[10],
                session[11]
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
