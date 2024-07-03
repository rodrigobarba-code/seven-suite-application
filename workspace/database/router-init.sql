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

/* Create 'add_router' stored procedure */
DELIMITER //

DROP PROCEDURE IF EXISTS add_router //

CREATE PROCEDURE sp_add_router (
    IN p_router_id VARCHAR(512),
    IN p_router_name VARCHAR(256),
    IN p_fk_site_id INT,
    IN p_fk_session_id INT,
    IN p_fk_ip_address_id INT
)
BEGIN
    DECLARE ip_valid INT DEFAULT 0;

    -- Check if the provided IP address ID exists and is valid
    SELECT COUNT(*)
    INTO ip_valid
    FROM ip_addresses_configuration
    WHERE ip_address_id = p_fk_ip_address_id;

    -- If IP is not valid, signal an error
    IF ip_valid = 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid IP address ID';
    ELSE
        -- Insert the router if the IP is valid
        INSERT INTO router (router_id, router_name, fk_site_id, fk_session_id, fk_ip_address_id)
        VALUES (p_router_id, p_router_name, p_fk_site_id, p_fk_session_id, p_fk_ip_address_id);
    END IF;
END //

DELIMITER ;
/* Create 'add_router' stored procedure */