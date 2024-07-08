/* Create 'router' table */
DROP TABLE IF EXISTS router;
CREATE TABLE router (
    router_id VARCHAR(512) NOT NULL PRIMARY KEY,
    router_name VARCHAR(256) NULL,
    fk_site_id INT NOT NULL,
    fk_session_id INT NULL,
    fk_ip_address_id INT NULL
);
/* Create 'router' table */

/* Alter table 'router' to include foreign keys */
ALTER TABLE router
ADD FOREIGN KEY (fk_site_id) REFERENCES site(site_id),
ADD FOREIGN KEY (fk_session_id) REFERENCES session_information(session_id),
ADD FOREIGN KEY (fk_ip_address_id) REFERENCES ip_addresses_configuration(ip_address_id);
/* Alter table 'router' to include foreign keys */

/* Stored Procedures */

/* Create 'sp_add_router' stored procedure */
DROP PROCEDURE IF EXISTS sp_add_router;
DELIMITER //
CREATE PROCEDURE sp_add_router(
    IN p_router_id VARCHAR(512),
    IN p_router_name VARCHAR(256),
    IN p_fk_site_id INT,
    IN p_fk_session_id INT,
    IN p_fk_ip_address_id INT
)
BEGIN
    INSERT INTO router(router_id, router_name, fk_site_id, fk_session_id, fk_ip_address_id)
    VALUES (p_router_id, p_router_name, p_fk_site_id, p_fk_session_id, p_fk_ip_address_id);
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
    IN p_fk_session_id INT,
    IN p_fk_ip_address_id INT
)
BEGIN
    UPDATE router
    SET router_name = p_router_name,
        fk_site_id = p_fk_site_id,
        fk_session_id = p_fk_session_id,
        fk_ip_address_id = p_fk_ip_address_id
    WHERE router_id = p_router_id;
END //
DELIMITER ;
/* Create 'sp_update_router' stored procedure */

/* Create 'sp_delete_router' stored procedure */
DROP PROCEDURE IF EXISTS sp_delete_router;
DELIMITER //
CREATE PROCEDURE sp_delete_router(
    IN p_router_id VARCHAR(512)
)
BEGIN
    DELETE FROM router WHERE router_id = p_router_id;
END //
DELIMITER ;
/* Create 'sp_delete_router' stored procedure */

/* Stored Procedures */