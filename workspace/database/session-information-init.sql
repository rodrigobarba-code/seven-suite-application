/* Create 'session_information' table */
DROP TABLE IF EXISTS session_information;
CREATE TABLE session_information
(
    session_id              INT PRIMARY KEY AUTO_INCREMENT,
    session_ip_address      VARCHAR(128) NOT NULL,
    session_mac_address     VARCHAR(128) NULL,
    session_username        VARCHAR(256) NOT NULL,
    session_password        VARCHAR(256) NOT NULL,
    session_connection_type VARCHAR(64)  NOT NULL,
    session_brand           VARCHAR(64)  NULL,
    session_model           VARCHAR(64)  NULL,
    allow_remote_access     BOOLEAN DEFAULT FALSE
);
/* Create 'session_information' table */

/* Create stored procedure 'sp_add_session_information' */
DROP PROCEDURE IF EXISTS sp_add_session_information;
DELIMITER //
CREATE PROCEDURE sp_add_session_information(
    IN p_session_ip_address VARCHAR(128),
    IN p_session_mac_address VARCHAR(128),
    IN p_session_username VARCHAR(256),
    IN p_session_password VARCHAR(256),
    IN p_session_connection_type VARCHAR(64),
    IN p_session_brand VARCHAR(64),
    IN p_session_model VARCHAR(64),
    IN p_allow_remote_access BOOLEAN
)
BEGIN
    DECLARE ip_valid BOOLEAN;
    DECLARE mac_valid BOOLEAN;
    DECLARE ip_exists BOOLEAN;
    DECLARE mac_exists BOOLEAN;
    SET ip_valid = FALSE;
    SET mac_valid = FALSE;
    SET ip_exists = FALSE;
    SET mac_exists = FALSE;
    IF p_session_ip_address REGEXP
       '^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$' THEN
        SET ip_valid = TRUE;
    END IF;
    IF p_session_mac_address REGEXP '^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$' THEN
        SET mac_valid = TRUE;
    END IF;
    IF ip_valid AND mac_valid THEN
        SELECT COUNT(*) INTO ip_exists FROM session_information WHERE session_ip_address = p_session_ip_address;
        SELECT COUNT(*) INTO mac_exists FROM session_information WHERE session_mac_address = p_session_mac_address;
        IF ip_exists = 0 AND mac_exists = 0 THEN
            INSERT INTO session_information(session_ip_address,
                                            session_mac_address,
                                            session_username,
                                            session_password,
                                            session_connection_type,
                                            session_brand,
                                            session_model,
                                            allow_remote_access)
            VALUES (p_session_ip_address,
                    p_session_mac_address,
                    p_session_username,
                    p_session_password,
                    p_session_connection_type,
                    p_session_brand,
                    p_session_model,
                    p_allow_remote_access);
        END IF;
    END IF;
END //
DELIMITER ;
/* Create stored procedure 'sp_add_session_information' */

/* Create stored procedure 'sp_delete_session_information_by_id' */
DROP PROCEDURE IF EXISTS sp_delete_session_information_by_id;
DELIMITER //
CREATE PROCEDURE sp_delete_session_information_by_id(
    IN p_session_id INT
)
BEGIN
    DELETE FROM session_information WHERE session_id = p_session_id;
END //
DELIMITER ;
/* Create stored procedure 'sp_delete_session_information_by_id' */

/* Create stored procedure 'sp_get_session_information_by_id' */
DROP PROCEDURE IF EXISTS sp_get_session_information_by_id;
DELIMITER //
CREATE PROCEDURE sp_get_session_information_by_id(
    IN p_session_id INT
)
BEGIN
    SELECT * FROM session_information WHERE session_id = p_session_id;
END //
DELIMITER ;
/* Create stored procedure 'sp_get_session_information_by_id' */

/* Create stored procedure 'sp_get_all_session_information' */
DROP PROCEDURE IF EXISTS sp_get_all_session_information;
DELIMITER //
CREATE PROCEDURE sp_get_all_session_information()
BEGIN
    SELECT * FROM session_information;
END //
DELIMITER ;
/* Create stored procedure 'sp_get_all_session_information' */

/* Create stored procedure 'sp_update_session_information_by_id'*/
DROP PROCEDURE IF EXISTS sp_update_session_information_by_id;
DELIMITER //
CREATE PROCEDURE sp_update_session_information_by_id(
    IN p_session_id INT,
    IN p_session_ip_address VARCHAR(128),
    IN p_session_mac_address VARCHAR(128),
    IN p_session_username VARCHAR(256),
    IN p_session_password VARCHAR(256),
    IN p_session_connection_type VARCHAR(64),
    IN p_session_brand VARCHAR(64),
    IN p_session_model VARCHAR(64),
    IN p_allow_remote_access BOOLEAN
)
BEGIN
    DECLARE ip_valid BOOLEAN;
    DECLARE mac_valid BOOLEAN;
    DECLARE ip_exists BOOLEAN;
    DECLARE mac_exists BOOLEAN;
    SET ip_valid = FALSE;
    SET mac_valid = FALSE;
    SET ip_exists = FALSE;
    SET mac_exists = FALSE;
    IF p_session_ip_address REGEXP
       '^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$' THEN
        SET ip_valid = TRUE;
    END IF;
    IF p_session_mac_address REGEXP '^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$' THEN
        SET mac_valid = TRUE;
    END IF;
    IF ip_valid AND mac_valid THEN
        SELECT COUNT(*) INTO ip_exists FROM session_information WHERE session_ip_address = p_session_ip_address;
        SELECT COUNT(*) INTO mac_exists FROM session_information WHERE session_mac_address = p_session_mac_address;
        IF ip_exists = 0 AND mac_exists = 0 THEN
            UPDATE session_information
            SET session_ip_address      = p_session_ip_address,
                session_mac_address     = p_session_mac_address,
                session_username        = p_session_username,
                session_password        = p_session_password,
                session_connection_type = p_session_connection_type,
                session_brand           = p_session_brand,
                session_model           = p_session_model,
                allow_remote_access     = p_allow_remote_access
            WHERE session_id = p_session_id;
        END IF;
    END IF;
END //
DELIMITER ;
/* Create stored procedure 'sp_update_session_information_by_id'*/
