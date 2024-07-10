/* Create 'session_port' table */
DROP TABLE IF EXISTS session_port;
CREATE TABLE session_port (
    session_port_id INT PRIMARY KEY AUTO_INCREMENT,
    fk_session_id INT NOT NULL,
    port_number INT NOT NULL,
    port_status BOOLEAN DEFAULT FALSE,
    port_protocol VARCHAR(64) NOT NULL,
    FOREIGN KEY (fk_session_id) REFERENCES session_information (session_id)
);
/* Create 'session_port' table */

/* Stored Procedures */

/* Create 'sp_add_session_port' stored procedure */
DELIMITER //
CREATE PROCEDURE sp_add_session_port(
    IN p_fk_session_id INT,
    IN p_port_number INT,
    IN p_port_protocol VARCHAR(64)
)
BEGIN
    INSERT INTO session_port (fk_session_id, port_number, port_protocol)
    VALUES (p_fk_session_id, p_port_number, p_port_protocol);
END //
DELIMITER ;
/* Create 'sp_add_session_port' stored procedure */

/* Create 'sp_get_session_port_by_id' stored procedure */
DELIMITER //
CREATE PROCEDURE sp_get_session_port_by_id(
    IN p_session_port_id INT
)
BEGIN
    SELECT * FROM session_port WHERE session_port_id = p_session_port_id;
END //
DELIMITER ;
/* Create 'sp_get_session_port_by_id' stored procedure */

/* Create 'sp_get_session_port_by_session_id' stored procedure */
DELIMITER //
CREATE PROCEDURE sp_get_session_port_by_session_id(
    IN p_fk_session_id INT
)
BEGIN
    SELECT * FROM session_port WHERE fk_session_id = p_fk_session_id;
END //
DELIMITER ;
/* Create 'sp_get_session_port_by_session_id' stored procedure */

/* Create 'sp_update_session_port' stored procedure */
DELIMITER //
CREATE PROCEDURE sp_update_session_port(
    IN p_port_number INT,
    IN p_port_status BOOLEAN,
    IN p_port_protocol VARCHAR(64)
)
BEGIN
    UPDATE session_port
    SET port_status = p_port_status
    SET port_number = p_port_number
    WHERE port_protocol = p_port_protocol;
END //
DELIMITER ;
/* Create 'sp_update_session_port' stored procedure */

/* Create 'sp_delete_session_port' stored procedure */
DELIMITER //
CREATE PROCEDURE sp_delete_all_session_ports (
    IN p_fk_session_id INT
)
BEGIN
    DELETE FROM session_port WHERE fk_session_id = p_fk_session_id;
END //
DELIMITER ;
/* Create 'sp_delete_session_port' stored procedure */

/* Stored Procedures */