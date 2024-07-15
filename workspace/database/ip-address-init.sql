/* Tables */
/* Create 'ip_address' table */
DROP TABLE IF EXISTS ip_address;
CREATE TABLE ip_address
(
    address_id INT NOT NULL PRIMARY KEY,
    fk_router_id INT NOT NULL,
    address_alias VARCHAR(128) NOT NULL,
    address_state VARCHAR(4) NULL,
    address_ip VARCHAR(16) NOT NULL,
    address_netmask VARCHAR(4) NOT NULL,
    address_interface VARCHAR(64) NOT NULL,
    address_network VARCHAR(16) NULL
);
/* Create 'ip_address' table */
/* Tables */

/* Stored Procedures */
/* Create stored procedure 'sp_if_ip_address_exists' */
DROP PROCEDURE IF EXISTS sp_if_ip_address_exists;
DELIMITER //
CREATE PROCEDURE sp_if_ip_address_exists
(
    IN p_address_ip VARCHAR(16),
    OUT p_exists INT
)
BEGIN
    -- Verify if the ip address exists
    IF EXISTS (SELECT 1 FROM ip_address WHERE ip_address.address_ip = p_address_ip) THEN
        SET p_exists = 1;
    ELSE
        SET p_exists = 0;
    END IF;
END //
/* Create stored procedure 'sp_if_ip_address_exists' */

/* Create stored procedure 'sp_get_address_id_by_ip' */
DROP PROCEDURE IF EXISTS sp_get_address_id_by_ip;
DELIMITER //
CREATE PROCEDURE sp_get_address_id_by_ip
(
    IN p_address_ip VARCHAR(16),
    OUT p_address_id INT
)
BEGIN
    -- Get the address_id by the ip address
    SELECT address_id INTO p_address_id FROM ip_address WHERE address_ip = p_address_ip;
END //
/* Create stored procedure 'sp_get_address_id_by_ip' */

/* Create stored procedure 'sp_add_ip_address' */
DROP PROCEDURE IF EXISTS sp_add_ip_address;
DELIMITER //
CREATE PROCEDURE sp_add_ip_address
(
    IN p_fk_router_id INT,
    IN p_address_alias VARCHAR(128),
    IN p_address_state VARCHAR(4),
    IN p_address_ip VARCHAR(16),
    IN p_address_netmask VARCHAR(4),
    IN p_address_interface VARCHAR(64),
    IN p_address_network VARCHAR(16)
)
BEGIN
    -- Declare variables
    DECLARE address_id INT;

    -- Assign the next minimum available identifier
    SELECT MIN(t1.address_id + 1) INTO address_id
    FROM ip_address t1
    LEFT JOIN ip_address t2 ON t1.address_id + 1 = t2.address_id
    WHERE t2.address_id IS NULL;

    -- If no address_id is available, assign the maximum identifier + 1
    IF address_id IS NULL THEN
        SELECT IFNULL(MAX(address_id), 0) + 1 INTO address_id FROM ip_address;
    END IF;

    -- Verify if the ip exists
    CALL sp_if_ip_address_exists(address_ip, @exists);

    IF @exists = 1 THEN
        -- Obtain id via ip address
        CALL sp_get_address_id_by_ip(address_ip, address_id);

        -- Update the ip address
        UPDATE ip_address SET fk_router_id = p_fk_router_id, address_alias = p_address_alias, address_state = p_address_state, address_ip = p_address_ip, address_netmask = p_address_netmask, address_interface = p_address_interface, address_network = p_address_network WHERE address_id = address_id;
    END IF;

    -- Insert the new ip address
    INSERT INTO ip_address(address_id, fk_router_id, address_alias, address_state, address_ip, address_netmask, address_interface, address_network) VALUES(address_id, p_fk_router_id, p_address_alias, p_address_state, p_address_ip, p_address_netmask, p_address_interface, p_address_network);
END //
DELIMITER ;
/* Create stored procedure 'sp_add_ip_address' */

/* Create stored procedure 'sp_update_ip_address' */
DROP PROCEDURE IF EXISTS sp_update_ip_address;
DELIMITER //
CREATE PROCEDURE sp_update_ip_address
(
    IN p_address_id INT,
    IN p_fk_router_id INT,
    IN p_address_alias VARCHAR(128),
    IN p_address_state VARCHAR(4),
    IN p_address_ip VARCHAR(16),
    IN p_address_netmask VARCHAR(4),
    IN p_address_interface VARCHAR(64),
    IN p_address_network VARCHAR(16)
)
BEGIN
    -- Verify if the ip address exists
    IF NOT EXISTS (SELECT 1 FROM ip_address WHERE ip_address.address_id = p_address_id) THEN
        SIGNAL SQLSTATE '45012'
        SET MESSAGE_TEXT = '45012 - IP address does not exist.';
    ELSE
        -- Update the ip address
        UPDATE ip_address SET fk_router_id = p_fk_router_id, address_alias = p_address_alias, address_state = p_address_state, address_ip = p_address_ip, address_netmask = p_address_netmask, address_interface = p_address_interface, address_network = p_address_network WHERE address_id = p_address_id;
    END IF;
END //
DELIMITER ;
/* Create stored procedure 'sp_update_ip_address' */

/* Create stored procedure 'sp_delete_ip_address' */
DROP PROCEDURE IF EXISTS sp_delete_ip_address;
DELIMITER //
CREATE PROCEDURE sp_delete_ip_address
(
    IN p_address_id INT
)
BEGIN
    -- Verify if the ip address exists
    IF NOT EXISTS (SELECT 1 FROM ip_address WHERE ip_address.address_id = p_address_id) THEN
        SIGNAL SQLSTATE '45012'
        SET MESSAGE_TEXT = '45012 - IP address does not exist.';
    ELSE
        -- Delete the ip address
        DELETE FROM ip_address WHERE address_id = p_address_id;
    END IF;
END //
DELIMITER ;
/* Create stored procedure 'sp_delete_ip_address' */
/* Stored Procedures */