/* Tables */
/* Create 'arp_list' table */
DROP TABLE IF EXISTS arp_list;
CREATE TABLE arp_list
(
    arp_id INT NOT NULL PRIMARY KEY,
    fk_router_id INT NOT NULL,
    arp_state VARCHAR(4) NULL DEFAULT NULL,
    arp_ip VARCHAR(16) NULL DEFAULT NULL,
    arp_mac VARCHAR(32) NULL DEFAULT NULL,
    arp_interface VARCHAR(32) NULL DEFAULT NULL,
    arp_netbios VARCHAR(256) NULL DEFAULT NULL,
    arp_set_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
/* Create 'arp_list' table */
/* Tables */

/* Stored Procedures */
/* Create stored procedure 'sp_add_arp_list' */
DROP PROCEDURE IF EXISTS sp_add_arp_list;
DELIMITER //
CREATE PROCEDURE sp_add_arp_list
(
    IN p_fk_router_id INT,
    IN p_arp_state VARCHAR(4),
    IN p_arp_ip VARCHAR(16),
    IN p_arp_mac VARCHAR(32),
    IN p_arp_interface VARCHAR(32),
    IN p_arp_netbios VARCHAR(256)
)
BEGIN
    -- Declare variables
    DECLARE arp_id INT;
    DECLARE arp_exists BOOLEAN;

    -- Initialize variables
    SET arp_exists = FALSE;

    -- Check if ARP entry already exists
    IF EXISTS (SELECT 1 FROM arp_list WHERE arp_list.fk_router_id = p_fk_router_id AND arp_list.arp_ip = p_arp_ip AND arp_list.arp_mac = p_arp_mac) THEN
        SET arp_exists = TRUE;
    END IF;

    -- If ARP entry does not exist, add it
    IF NOT arp_exists THEN
        -- Assign the next minimum available identifier
        SELECT MIN(t1.arp_id + 1) INTO arp_id
        FROM arp_list t1
        LEFT JOIN arp_list t2 ON t1.arp_id + 1 = t2.arp_id
        WHERE t2.arp_id IS NULL;

        -- If no arp_id is available, assign the maximum identifier + 1
        IF arp_id IS NULL THEN
            SELECT IFNULL(MAX(arp_id), 0) + 1 INTO arp_id FROM arp_list;
        END IF;

        -- Insert the new ARP entry
        INSERT INTO arp_list(arp_id, fk_router_id, arp_state, arp_ip, arp_mac, arp_interface, arp_netbios) VALUES(arp_id, p_fk_router_id, p_arp_state, p_arp_ip, p_arp_mac, p_arp_interface, p_arp_netbios);
    END IF;
END //
DELIMITER ;
/* Create stored procedure 'sp_add_arp_list' */

/* Create stored procedure 'sp_delete_arp_list' */
DROP PROCEDURE IF EXISTS sp_delete_arp_list;
DELIMITER //
CREATE PROCEDURE sp_delete_arp_list
(
    IN p_arp_id INT
)
BEGIN
    -- Verify if the ARP entry exists
    IF NOT EXISTS (SELECT 1 FROM arp_list WHERE arp_list.arp_id = p_arp_id) THEN
        SIGNAL SQLSTATE '45014'
        SET MESSAGE_TEXT = '45014 - ARP entry does not exist.';
    ELSE
        -- Delete the ARP entry
        DELETE FROM arp_list WHERE arp_list.arp_id = p_arp_id;
    END IF;
END //
DELIMITER ;
/* Create stored procedure 'sp_delete_arp_list' */

/* Create stored procedure 'sp_get_arp_column' */
DROP PROCEDURE IF EXISTS sp_get_arp_column;
DELIMITER //
CREATE PROCEDURE sp_get_arp_column
(
    IN p_arp_id INT,
    IN p_column_name VARCHAR(32)
)
BEGIN
    -- Declare variables
    DECLARE arp_column_value VARCHAR(256);

    -- Initialize variables
    SET arp_column_value = NULL;

    -- Verify if the ARP entry exists
    IF NOT EXISTS (SELECT 1 FROM arp_list WHERE arp_list.arp_id = p_arp_id) THEN
        SIGNAL SQLSTATE '45014'
        SET MESSAGE_TEXT = '45014 - ARP entry does not exist.';
    ELSE
        -- Get the ARP column value
        SELECT p_column_name INTO arp_column_value FROM arp_list WHERE arp_list.arp_id = p_arp_id;
    END IF;

    -- Return the ARP column value
    SELECT arp_column_value;
END //
DELIMITER ;
/* Create stored procedure 'sp_get_arp_column' */

/* Create stored procedure 'sp_get_arp_list' */
DROP PROCEDURE IF EXISTS sp_get_arp_list;
DELIMITER //
CREATE PROCEDURE sp_get_arp_list()
BEGIN
    -- Get all ARP entries
    SELECT arp_id, fk_router_id, arp_state, arp_ip, arp_mac, arp_interface, arp_netbios, arp_set_date FROM arp_list;
END //
DELIMITER ;
/* Create stored procedure 'sp_get_arp_list' */

/* Create stored procedure 'sp_get_arp_list_by_router' */
DROP PROCEDURE IF EXISTS sp_get_arp_list_by_router;
DELIMITER //
CREATE PROCEDURE sp_get_arp_list_by_router
(
    IN p_fk_router_id INT
)
BEGIN
    -- Verify if the router exists
    IF NOT EXISTS (SELECT 1 FROM router WHERE router.router_id = p_fk_router_id) THEN
        SIGNAL SQLSTATE '45011'
        SET MESSAGE_TEXT = '45011 - Router does not exist.';
    ELSE
        -- Get all ARP entries for the router
        SELECT arp_id, fk_router_id, arp_state, arp_ip, arp_mac, arp_interface, arp_netbios, arp_set_date FROM arp_list WHERE arp_list.fk_router_id = p_fk_router_id;
    END IF;
END //
DELIMITER ;
/* Create stored procedure 'sp_get_arp_list_by_router' */
/* Stored Procedures */