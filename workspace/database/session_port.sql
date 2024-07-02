/* Create 'session_port' table */
DROP TABLE IF EXISTS session_port;
CREATE TABLE session_port (
    session_port_id INT,
    fk_session_id INT,
    port_number INT,
    port_status BOOLEAN,
    port_protocol VARCHAR(64),
    FOREIGN KEY (fk_session_id) REFERENCES session_information (session_id)
);
/* Create 'session_port' table */