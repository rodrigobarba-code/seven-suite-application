/* Create 'router' table */
DROP TABLE IF EXISTS router;
CREATE TABLE router (
    router_id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    router_name VARCHAR(256) NULL,
    router_description VARCHAR(512) NULL,
    fk_site_id INT NOT NULL,
    fk_session_id INT NULL
);
/* Create 'router' table */

/* Alter table 'router' to include foreign keys */
ALTER TABLE router
MODIFY COLUMN router_id INT NOT NULL AUTO_INCREMENT,
ADD FOREIGN KEY (fk_site_id) REFERENCES site(site_id),
ADD FOREIGN KEY (fk_session_id) REFERENCES session_information(session_id),
ADD FOREIGN KEY (fk_ip_address_id) REFERENCES ip_addresses_configuration(ip_address_id);
/* Alter table 'router' to include foreign keys */

/* Stored Procedures */

/* Create 'sp_add_router' stored procedure */
DROP PROCEDURE IF EXISTS sp_add_router;
DELIMITER //
CREATE PROCEDURE sp_add_router(
    IN p_router_name VARCHAR(256),
    IN p_fk_site_id INT,
    IN p_fk_session_id INT,
    IN p_fk_ip_address_id INT
)
BEGIN
    /* Date in string format*/
    INSERT INTO router(router_name, fk_site_id, fk_session_id, fk_ip_address_id)
    VALUES (p_router_name, p_fk_site_id, p_fk_session_id, p_fk_ip_address_id);
END //
DELIMITER ;
/* Create 'sp_add_router' stored procedure */

/* Create 'sp_get_router_by_id' stored procedure */
DROP PROCEDURE IF EXISTS sp_get_router_by_id;
DELIMITER //
CREATE PROCEDURE sp_get_router_by_id(
    IN p_router_id VARCHAR(512)
)
BEGIN
    SELECT * FROM router WHERE router_id = p_router_id;
END //
DELIMITER ;
/* Create 'sp_get_router_by_id' stored procedure */

/* Create 'sp_get_all_routers' stored procedure */
DROP PROCEDURE IF EXISTS sp_get_all_routers;
DELIMITER //
CREATE PROCEDURE sp_get_all_routers()
BEGIN
    SELECT * FROM router;
END //
DELIMITER ;
/* Create 'sp_get_all_routers' stored procedure */

/* Create 'sp_update_router' stored procedure */
DROP PROCEDURE IF EXISTS sp_update_router;
DELIMITER //
CREATE PROCEDURE sp_update_router(
    IN p_router_id VARCHAR(512),
    IN p_router_name VARCHAR(256),
    IN p_fk_site_id INT,
    IN p_fk_ip_address_id INT
)
BEGIN
    UPDATE router
    SET router_name = p_router_name,
        fk_site_id = p_fk_site_id,
        fk_ip_address_id = p_fk_ip_address_id
    WHERE router_id = p_router_id;
END //
DELIMITER ;
/* Create 'sp_update_router' stored procedure */

/* Create 'sp_delete_router' stored procedure */
DROP PROCEDURE IF EXISTS sp_delete_router;
DELIMITER //
CREATE PROCEDURE sp_delete_router(
    IN p_router_id VARCHAR(512),
    IN p_session_id INT
)
BEGIN
    DELETE FROM router WHERE router_id = p_router_id;
    IF p_session_id IS NOT NULL THEN
        DELETE FROM session_information WHERE session_id = p_session_id;
    END IF;
END //
DELIMITER ;
/* Create 'sp_delete_router' stored procedure */

/* Create 'sp_add_router_with_session_information' stored procedure */
DROP PROCEDURE IF EXISTS sp_add_router_with_session_information;
DELIMITER //
CREATE PROCEDURE sp_add_router_with_session_information(
    IN p_router_name VARCHAR(256),
    IN p_fk_site_id INT,
    IN p_fk_session_id INT,
    IN p_fk_ip_address_id INT,
    IN p_session_ip_address VARCHAR(128),
    IN p_session_mac_address VARCHAR(128),
    IN p_session_username VARCHAR(256),
    IN p_session_password VARCHAR(256),
    IN p_session_connection_type VARCHAR(128),
    IN p_session_brand VARCHAR(128),
    IN p_session_model VARCHAR(128),
    IN p_allow_remote_access BOOLEAN
)
BEGIN
    DECLARE v_session_id INT;

    CALL sp_add_session_information(
        p_session_ip_address,
        p_session_mac_address,
        p_session_username,
        p_session_password,
        p_session_connection_type,
        p_session_brand,
        p_session_model,
        p_allow_remote_access
    );

    -- Ensure LAST_INSERT_ID() is called immediately after the INSERT operation
    SELECT session_id INTO v_session_id FROM session_information WHERE session_id = LAST_INSERT_ID();

    -- Verify v_session_id is valid (not NULL or 0) before proceeding
    IF v_session_id IS NOT NULL AND v_session_id > 0 THEN
        CALL sp_add_router(p_router_name, p_fk_site_id, v_session_id, p_fk_ip_address_id);
    ELSE
        -- Handle error: v_session_id is not valid
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Failed to retrieve valid session_id from session_information';
    END IF;
END //
DELIMITER ;
/* Create 'sp_add_router_with_session_information' stored procedure */

/* Stored Procedures */