from .entities.session_port import SessionPort

class ModelSessionPort:

    @classmethod
    def add_session_port(self, db, session_port):
        try:
            cursor = db.connection.cursor()
            cursor.execute("CALL sp_add_session_port(%s, %s, %s, %s, %s)", (
                session_port.fk_session_id,
                session_port.port_number,
                session_port.port_status,
                session_port.port_protocol
            ))
            db.connection.commit()
        except Exception as ex:
            raise Exception(ex)

