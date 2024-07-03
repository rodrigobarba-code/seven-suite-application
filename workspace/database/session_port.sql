/* Create 'session_port.py' table */
DROP TABLE IF EXISTS session_port;
CREATE TABLE session_port (
    session_port_id INT PRIMARY KEY AUTO_INCREMENT,
    fk_session_id INT NOT NULL,
    port_number INT NOT NULL,
    port_status BOOLEAN DEFAULT FALSE,
    port_protocol VARCHAR(64) NOT NULL,
    FOREIGN KEY (fk_session_id) REFERENCES session_information (session_id)
);
/* Create 'session_port.py' table */