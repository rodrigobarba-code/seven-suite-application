/* Tables */
/* Create 'router' table */
DROP TABLE IF EXISTS router;
CREATE TABLE router (
    router_id VARCHAR(36) NOT NULL PRIMARY KEY,
    router_name VARCHAR(256) NULL,
    router_description VARCHAR(512) NULL,
    fk_site_id INT NULL,
    fk_session_id INT NULL
);
/* Create 'router' table */

/* Alter table 'router' to include foreign keys */
ALTER TABLE router
ADD FOREIGN KEY (fk_site_id) REFERENCES site(site_id),
ADD FOREIGN KEY (fk_session_id) REFERENCES session_information(session_id);
/* Alter table 'router' to include foreign keys */
/* Tables */

/* Stored Procedures */
/* Create 'sp_add_router' stored procedure */
DROP PROCEDURE IF EXISTS sp_add_router;
DELIMITER //
CREATE PROCEDURE sp_add_router
(
    IN p_router_name VARCHAR(256),
    IN p_router_description VARCHAR(512),
    IN p_fk_site_id INT
)
BEGIN
    DECLARE router_id INT;
    DECLARE session_id INT;
    DECLARE t_region_id INT;
    DECLARE t_site_id INT;

    -- Verify if the router name already exists
    IF EXISTS (SELECT 1 FROM router WHERE LOWER(router.router_name) = LOWER(p_router_name)) THEN
        SIGNAL SQLSTATE '45010'
        SET MESSAGE_TEXT = '45010 - Router already exists.';
    ELSE
        -- Create identifier with region_id in two digits, site_id in two digits and datetime in format YYMMDDHHMM
        SELECT fk_region_id INTO t_region_id FROM site WHERE site_id = p_fk_site_id;
        SELECT site_id INTO t_site_id FROM site WHERE site_id = p_fk_site_id;
        SET router_id = (SELECT CONCAT(t_region_id, t_site_id));

        -- Verify if the router_id already exists
        IF EXISTS (SELECT 1 FROM router WHERE router.router_id = router_id) THEN
            SIGNAL SQLSTATE '45015'
            SET MESSAGE_TEXT = '45015 - Can only have one router per site.';
        ELSE
            -- Create the session_id from sp_add_session_only
            CALL sp_add_session_only(session_id);

            -- Insert the new router
            INSERT INTO router(router_id, router_name, router_description, fk_site_id, fk_session_id) VALUES(router_id, p_router_name, p_router_description, p_fk_site_id, session_id);
        END IF;
    END IF;
END //
DELIMITER ;
/* Create 'sp_add_router' stored procedure */

/* Create 'sp_update_router' stored procedure */
DROP PROCEDURE IF EXISTS sp_update_router;
DELIMITER //
CREATE PROCEDURE sp_update_router
(
    IN p_router_id INT,
    IN p_router_name VARCHAR(256),
    IN p_router_description VARCHAR(512),
    IN p_fk_site_id INT,
    IN p_fk_session_id INT
)
BEGIN
    -- Verify if the router exists
    IF NOT EXISTS (SELECT 1 FROM router WHERE router.router_id = p_router_id) THEN
        SIGNAL SQLSTATE '45011'
        SET MESSAGE_TEXT = '45011 - Router does not exist.';
    ELSE
        -- Verify if the router name already exists
        IF EXISTS (SELECT 1 FROM router WHERE LOWER(router.router_name) = LOWER(p_router_name) AND router.router_id != p_router_id) THEN
            SIGNAL SQLSTATE '45012'
            SET MESSAGE_TEXT = '45010 - Router already exists.';
        ELSE
            -- Update the router
            UPDATE router
            SET router_name = p_router_name,
                router_description = p_router_description,
                fk_site_id = p_fk_site_id,
                fk_session_id = p_fk_session_id
            WHERE router_id = p_router_id;
        END IF;
    END IF;
END //
DELIMITER ;
/* Create 'sp_update_router' stored procedure */

/* Create 'sp_delete_router' stored procedure */
DROP PROCEDURE IF EXISTS sp_delete_router;
DELIMITER //
CREATE PROCEDURE sp_delete_router
(
    IN p_router_id INT
)
BEGIN
    -- Verify if the router exists
    IF NOT EXISTS (SELECT 1 FROM router WHERE router.router_id = p_router_id) THEN
        SIGNAL SQLSTATE '45012'
        SET MESSAGE_TEXT = '45012 - Router does not exist.';
    ELSE
        -- Verify if the router is being used by a site
        IF EXISTS (SELECT 1 FROM site WHERE site.fk_router_id = p_router_id) THEN
            SIGNAL SQLSTATE '45013'
            SET MESSAGE_TEXT = '45013 - Router is being used in a Site.';
        ELSE
        -- Delete the router
        DELETE FROM router WHERE router_id = p_router_id;
        END IF;
    END IF;
END //
DELIMITER ;
/* Create 'sp_delete_router' stored procedure */

/* Create 'sp_get_router' stored procedure */
DROP PROCEDURE IF EXISTS sp_get_router;
DELIMITER //
CREATE PROCEDURE sp_get_router
(
    IN p_router_id INT
)
BEGIN
    -- Verify if the router exists
    IF NOT EXISTS (SELECT 1 FROM router WHERE router.router_id = p_router_id) THEN
        SIGNAL SQLSTATE '45012'
        SET MESSAGE_TEXT = '45012 - Router does not exist.';
    ELSE
        -- Get the router
        SELECT router_id, router_name, router_description, fk_site_id, fk_session_id FROM router WHERE router_id = p_router_id;
    END IF;
END //
DELIMITER ;
/* Create 'sp_get_router' stored procedure */

/* Create 'sp_get_routers' stored procedure */
DROP PROCEDURE IF EXISTS sp_get_routers;
DELIMITER //
CREATE PROCEDURE sp_get_routers()
BEGIN
    -- Get all routers
    SELECT router_id, router_name, router_description, fk_site_id, fk_session_id FROM router;
END //
DELIMITER ;
/* Create 'sp_get_routers' stored procedure */
/* Stored Procedures */