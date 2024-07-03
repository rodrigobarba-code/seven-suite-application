/* Create 'session_information' table */
DROP TABLE IF EXISTS session_information;
CREATE TABLE session_information (
    session_id INT PRIMARY KEY AUTO_INCREMENT,
    session_ip_address VARCHAR(128) NOT NULL,
    session_mac_address VARCHAR(128) NULL,
    session_username VARCHAR(256) NOT NULL,
    session_password VARCHAR(256) NOT NULL,
    session_connection_type VARCHAR(64) NOT NULL,
    session_brand VARCHAR(64) NULL,
    session_model VARCHAR(64) NULL,
    allow_remote_access BOOLEAN DEFAULT FALSE
);
/* Create 'session_information' table */