/* Tables */
/* Create 'site' table */
DROP TABLE IF EXISTS site;
CREATE TABLE site (
    site_id INT NOT NULL PRIMARY KEY,
    fk_region_id INT NOT NULL,
    site_name VARCHAR(128) NOT NULL,
    site_segment INT NOT NULL,
    FOREIGN KEY (fk_region_id) REFERENCES region (region_id)
);
/* Create 'site' table */
/* Tables */

/* Stored Procedures */
/* Create stored procedure 'sp_add_site' */
DROP PROCEDURE IF EXISTS sp_add_site;
DELIMITER //
CREATE PROCEDURE sp_add_site
(
    IN fk_region_id INT,
    IN site_name VARCHAR(128),
    IN site_segment INT
)
BEGIN
    DECLARE site_id INT;

    -- Verify if the site name already exists
    IF EXISTS (SELECT 1 FROM site WHERE LOWER(site.site_name) = LOWER(site_name)) THEN
        SIGNAL SQLSTATE '45004'
        SET MESSAGE_TEXT = '45004 - Site already exists.';
    ELSE
        -- Assign the next minimum available identifier
        SELECT MIN(t1.site_id + 1) INTO site_id
        FROM site t1
        LEFT JOIN site t2 ON t1.site_id + 1 = t2.site_id
        WHERE t2.site_id IS NULL;

        -- If no site_id is available, assign the maximum identifier + 1
        IF site_id IS NULL THEN
            SELECT IFNULL(MAX(site_id), 0) + 1 INTO site_id FROM site;
        END IF;

        -- Insert the new site
        INSERT INTO site(site_id, fk_region_id, site_name, site_segment) VALUES(site_id, fk_region_id, site_name, site_segment);
    END IF;
END //
DELIMITER ;
/* Create stored procedure 'sp_add_site' */

/* Create stored procedure 'sp_update_site' */
DROP PROCEDURE IF EXISTS sp_update_site;
DELIMITER //
CREATE PROCEDURE sp_update_site
(
    IN site_id INT,
    IN fk_region_id INT,
    IN site_name VARCHAR(128),
    IN site_segment INT
)
BEGIN
    -- Verify if the site exists
    IF NOT EXISTS (SELECT 1 FROM site WHERE site.site_id = site_id) THEN
        SIGNAL SQLSTATE '45005'
        SET MESSAGE_TEXT = '45005 - Site does not exist.';
    ELSE
        -- Verify if the site name already exists
        IF EXISTS (SELECT 1 FROM site WHERE LOWER(site.site_name) = LOWER(site_name) AND site.site_id != site_id) THEN
            SIGNAL SQLSTATE '45004'
            SET MESSAGE_TEXT = '45004 - Site already exists.';
        ELSE
            -- Update the site
            UPDATE site SET site.fk_region_id = fk_region_id, site.site_name = site_name, site.site_segment = site_segment WHERE site.site_id = site_id;
        END IF;
    END IF;
END //
DELIMITER ;
/* Create stored procedure 'sp_update_site' */

/* Create stored procedure 'sp_delete_site' */
DROP PROCEDURE IF EXISTS sp_delete_site;
DELIMITER //
CREATE PROCEDURE sp_delete_site
(
    IN site_id INT
)
BEGIN
    -- Verify if the site exists
    IF NOT EXISTS (SELECT 1 FROM site WHERE site.site_id = site_id) THEN
        SIGNAL SQLSTATE '45005'
        SET MESSAGE_TEXT = '45005 - Site does not exist.';
    ELSE
        -- Delete the site
        DELETE FROM site WHERE site.site_id = site_id;
    END IF;
END //
DELIMITER ;
/* Create stored procedure 'sp_delete_site' */

/* Create stored procedure 'sp_get_site' */
DROP PROCEDURE IF EXISTS sp_get_site;
DELIMITER //
CREATE PROCEDURE sp_get_site
(
    IN site_id INT
)
BEGIN
    -- Verify if the site exists
    IF NOT EXISTS (SELECT 1 FROM site WHERE site.site_id = site_id) THEN
        SIGNAL SQLSTATE '45005'
        SET MESSAGE_TEXT = '45005 - Site does not exist.';
    ELSE
        -- Get the site
        SELECT site_id, fk_region_id, site_name, site_segment FROM site WHERE site.site_id = site_id;
    END IF;
END //
DELIMITER ;
/* Create stored procedure 'sp_get_site' */

/* Create stored procedure 'sp_get_sites' */
DROP PROCEDURE IF EXISTS sp_get_sites;
DELIMITER //
CREATE PROCEDURE sp_get_sites()
BEGIN
    -- Get all sites
    SELECT site_id, fk_region_id, site_name, site_segment FROM site;
END //
DELIMITER ;
/* Create stored procedure 'sp_get_sites' */

/* Create stored procedure 'sp_get_region_name' */
DROP PROCEDURE IF EXISTS sp_get_region_name;
DELIMITER //
CREATE PROCEDURE sp_get_region_name
(
    IN site_name VARCHAR(128)
)
BEGIN
    -- Verify if the site exists
    IF NOT EXISTS (SELECT 1 FROM site WHERE site.site_name = site_name) THEN
        SIGNAL SQLSTATE '45005'
        SET MESSAGE_TEXT = '45005 - Site does not exist.';
    ELSE
        -- Get the region name
        SELECT region_name FROM region WHERE region_id = (SELECT fk_region_id FROM site WHERE site.site_name = site_name);
    END IF;
END //
/* Create stored procedure 'sp_get_region_name' */