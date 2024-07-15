/* Tables */
/* Create 'session_information' table */
DROP TABLE IF EXISTS session_information;
CREATE TABLE session_information
(
    session_id INT NOT NULL PRIMARY KEY,
    session_ip VARCHAR(16) NULL DEFAULT NULL,
    session_mac VARCHAR(32) NULL DEFAULT NULL,
    session_username VARCHAR(128) NULL DEFAULT NULL,
    session_password VARCHAR(128) NULL DEFAULT NULL,
    session_via ENUM('API', 'API_SSL') NULL DEFAULT NULL,
    api_port INT NULL DEFAULT NULL,
    api_port_ssl INT NULL DEFAULT NULL,
    allow_scan BOOLEAN NULL DEFAULT FALSE
);
/* Create 'session_information' table */
/* Tables */

/* Stored Procedures */
/* Create stored procedure 'sp_add_session_information' */
DROP PROCEDURE IF EXISTS sp_add_session_information;
DELIMITER //
CREATE PROCEDURE sp_add_session_information
(
    IN p_session_mac VARCHAR(32),
    IN p_session_username VARCHAR(128),
    IN p_session_password VARCHAR(128),
    IN p_session_via ENUM('API', 'API_SSL'),
    IN p_api_port INT,
    IN p_api_port_ssl INT,
    IN p_allow_scan BOOLEAN
)
BEGIN
    -- Declare variables
    DECLARE session_id INT;
    DECLARE ip_valid BOOLEAN;
    DECLARE mac_valid BOOLEAN;
    DECLARE ip_exists BOOLEAN;
    DECLARE mac_exists BOOLEAN;

    -- Initialize variables
    SET ip_valid = FALSE;
    SET mac_valid = FALSE;
    SET ip_exists = FALSE;
    SET mac_exists = FALSE;

    -- Validate IP address
    IF p_session_ip REGEXP
       '^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$' THEN
        SET ip_valid = TRUE;
    END IF;

    -- Validate MAC address
    IF p_session_mac REGEXP '^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$' THEN
        SET mac_valid = TRUE;
    END IF;

    -- Check if IP address is valid
    IF ip_valid THEN
       -- Check if MAC address is valid
        IF mac_valid THEN
            SELECT COUNT(*) INTO ip_exists FROM session_information WHERE session_ip = p_session_ip;
            SELECT COUNT(*) INTO mac_exists FROM session_information WHERE session_mac = p_session_mac;

            -- Check if IP and MAC address already exists
            IF ip_exists = 0 AND mac_exists = 0 THEN
                -- Assign the next minimum available identifier
                SELECT MIN(t1.session_id + 1) INTO session_id
                FROM session_information t1
                LEFT JOIN session_information t2 ON t1.session_id + 1 = t2.session_id
                WHERE t2.session_id IS NULL;

                -- If no session_id is available, assign the maximum identifier + 1
                IF session_id IS NULL THEN
                    SELECT IFNULL(MAX(session_id), 0) + 1 INTO session_id FROM session_information;
                END IF;

                -- Insert the new session
                INSERT INTO session_information(session_id, session_ip, session_mac, session_username, session_password, session_via, api_port, api_port_ssl, allow_scan) VALUES(session_id, p_session_ip, p_session_mac, p_session_username, p_session_password, p_session_via, p_api_port, p_api_port_ssl, p_allow_scan);
            ELSE
                SIGNAL SQLSTATE '45008'
                SET MESSAGE_TEXT = '45008 - Session already exists.';
            END IF;
        ELSE
            SIGNAL SQLSTATE '45007'
            SET MESSAGE_TEXT = '45007 - Invalid MAC address.';
        END IF;
    ELSE
        SIGNAL SQLSTATE '45006'
        SET MESSAGE_TEXT = '45006 - Invalid IP address.';
    END IF;
END //
/* Create stored procedure 'sp_add_session_information' */

/* Create stored procedure 'sp_update_session_information' */
DROP PROCEDURE IF EXISTS sp_update_session_information;
DELIMITER //
CREATE PROCEDURE sp_update_session_information
(
    IN p_session_id INT,
    IN p_session_ip VARCHAR(16),
    IN p_session_mac VARCHAR(32),
    IN p_session_username VARCHAR(128),
    IN p_session_password VARCHAR(128),
    IN p_session_via ENUM('API', 'API_SSL'),
    IN p_api_port INT,
    IN p_api_port_ssl INT,
    IN p_allow_scan BOOLEAN
)
BEGIN
    -- Declare variables
    DECLARE ip_valid BOOLEAN;
    DECLARE mac_valid BOOLEAN;
    DECLARE ip_exists BOOLEAN;
    DECLARE mac_exists BOOLEAN;

    -- Initialize variables
    SET ip_valid = FALSE;
    SET mac_valid = FALSE;
    SET ip_exists = FALSE;
    SET mac_exists = FALSE;

    -- Validate IP address
    IF p_session_ip REGEXP
       '^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$' THEN
        SET ip_valid = TRUE;
    END IF;

    -- Validate MAC address
    IF p_session_mac REGEXP '^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$' THEN
        SET mac_valid = TRUE;
    END IF;

    -- Check if IP address is valid
    IF ip_valid THEN
       -- Check if MAC address is valid
        IF mac_valid THEN
            SELECT COUNT(*) INTO ip_exists FROM session_information WHERE session_ip = p_session_ip AND session_id != p_session_id;
            SELECT COUNT(*) INTO mac_exists FROM session_information WHERE session_mac = p_session_mac AND session_id != p_session_id;

            -- Check if IP and MAC address already exists
            IF ip_exists = 0 AND mac_exists = 0 THEN
                -- Update the session
                UPDATE session_information SET session_ip = p_session_ip, session_mac = p_session_mac, session_username = p_session_username, session_password = p_session_password, session_via = p_session_via, api_port = p_api_port, api_port_ssl = p_api_port_ssl, allow_scan = p_allow_scan WHERE session_id = p_session_id;
            ELSE
                SIGNAL SQLSTATE '45008'
                SET MESSAGE_TEXT = '45008 - Session already exists.';
            END IF;
        ELSE
            SIGNAL SQLSTATE '45007'
            SET MESSAGE_TEXT = '45007 - Invalid MAC address.';
        END
    ELSE
        SIGNAL SQLSTATE '45006'
        SET MESSAGE_TEXT = '45006 - Invalid IP address.';
    END IF;
END //
/* Create stored procedure 'sp_update_session_information' */

/* Create stored procedure 'sp_delete_session_information' */
DROP PROCEDURE IF EXISTS sp_delete_session_information;
DELIMITER //
CREATE PROCEDURE sp_delete_session_information
(
    IN p_session_id INT
)
BEGIN
    -- Verify if the session exists
    IF NOT EXISTS (SELECT 1 FROM session_information WHERE session_id = p_session_id) THEN
        SIGNAL SQLSTATE '45009'
        SET MESSAGE_TEXT = '45009 - Session does not exist.';
    ELSE
        -- Delete the session
        DELETE FROM session_information WHERE session_id = p_session_id;
    END IF;
END //
/* Create stored procedure 'sp_delete_session_information' */

/* Create stored procedure 'sp_get_session_information' */
DROP PROCEDURE IF EXISTS sp_get_session_information;
DELIMITER //
CREATE PROCEDURE sp_get_session_information
(
    IN p_session_id INT
)
BEGIN
    -- Verify if the session exists
    IF NOT EXISTS (SELECT 1 FROM session_information WHERE session_id = p_session_id) THEN
        SIGNAL SQLSTATE '45009'
        SET MESSAGE_TEXT = '45009 - Session does not exist.';
    ELSE
        -- Get the session
        SELECT session_id, session_ip, session_mac, session_username, session_password, session_via, api_port, api_port_ssl, allow_scan FROM session_information WHERE session_id = p_session_id;
    END IF;
END //
/* Create stored procedure 'sp_get_session_information' */

/* Create stored procedure 'sp_get_sessions_information' */
DROP PROCEDURE IF EXISTS sp_get_sessions_information;
DELIMITER //
CREATE PROCEDURE sp_get_sessions_information()
BEGIN
    -- Get all sessions
    SELECT session_id, session_ip, session_mac, session_username, session_password, session_via, api_port, api_port_ssl, allow_scan FROM session_information;
END //
/* Create stored procedure 'sp_get_sessions_information' */
/* Stored Procedures */