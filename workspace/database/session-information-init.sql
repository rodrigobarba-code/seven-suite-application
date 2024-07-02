/* Create 'session_information' table */
DROP TABLE IF EXISTS session_information;
CREATE TABLE session_information (
    session_id INT PRIMARY KEY AUTO_INCREMENT,
    session_hostname VARCHAR(512),
    session_username VARCHAR(256),
    session_password VARCHAR(256),
    session_connection_type VARCHAR(64),
    session_brand VARCHAR(64),
    session_model VARCHAR(64),
    allow_remote_access BOOLEAN
);
/* Create 'session_information' table */