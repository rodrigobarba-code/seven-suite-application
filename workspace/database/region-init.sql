/* Tables */
/* Create 'regions' table */
DROP TABLE IF EXISTS region;
CREATE TABLE region
(
    region_id INT NOT NULL PRIMARY KEY,
    region_name VARCHAR(128) NOT NULL
);
/* Create 'regions' table */
/* Tables */

/* Stored Procedures */
/* Create stored procedure 'sp_add_region' */
DROP PROCEDURE IF EXISTS sp_add_region;
DELIMITER //
CREATE PROCEDURE sp_add_region
(
    IN region_name VARCHAR(128)
)
BEGIN
    DECLARE region_id INT;

    -- Verify if the region name already exists
    IF EXISTS (SELECT 1 FROM region WHERE LOWER(region.region_name) = LOWER(region_name)) THEN
        SIGNAL SQLSTATE '45001'
        SET MESSAGE_TEXT = '45001 - Region name already exists.';
    ELSE
        -- Assign the next minimum available identifier
        SELECT MIN(t1.region_id + 1) INTO region_id
        FROM region t1
        LEFT JOIN region t2 ON t1.region_id + 1 = t2.region_id
        WHERE t2.region_id IS NULL;

        -- If no region_id is available, assign the maximum identifier + 1
        IF region_id IS NULL THEN
            SELECT IFNULL(MAX(region_id), 0) + 1 INTO region_id FROM region;
        END IF;

        -- Insert the new region
        INSERT INTO region(region_id, region_name) VALUES(region_id, region_name);
    END IF;
END //
DELIMITER ;
/* Create stored procedure 'sp_add_region' */

/* Create stored procedure 'sp_update_region' */
DROP PROCEDURE IF EXISTS sp_update_region;
DELIMITER //
CREATE PROCEDURE sp_update_region
(
    IN region_id INT,
    IN region_name VARCHAR(128)
)
BEGIN
    -- Verify if the region exists
    IF NOT EXISTS (SELECT 1 FROM region WHERE region.region_id = region_id) THEN
        SIGNAL SQLSTATE '45002'
        SET MESSAGE_TEXT = '45002 - Region does not exist.';
    ElSE
        -- Verify if the region name already exists
        IF EXISTS (SELECT 1 FROM region WHERE LOWER(region.region_name) = LOWER(region_name)) THEN
            SIGNAL SQLSTATE '45001'
            SET MESSAGE_TEXT = '45001 - Region name already exists.';
        ELSE
            -- Update the region
            UPDATE region SET region_name = region_name WHERE region.region_id = region_id;
        END IF;
    END IF;
END //
DELIMITER ;
/* Create stored procedure 'sp_update_region' */

/* Create stored procedure 'sp_delete_region' */
DROP PROCEDURE IF EXISTS sp_delete_region;
DELIMITER //
CREATE PROCEDURE sp_delete_region
(
    IN region_id INT
)
BEGIN
    -- Verify if the region exists
    IF NOT EXISTS (SELECT 1 FROM region WHERE region.region_id = region_id) THEN
        SIGNAL SQLSTATE '45002'
        SET MESSAGE_TEXT = '45002 - Region does not exist.';
    ELSE
        -- Verify if the region is being used
        IF EXISTS (SELECT 1 FROM site WHERE site.fk_region_id = region_id) THEN
            SIGNAL SQLSTATE '45003'
            SET MESSAGE_TEXT = '45003 - Region is being used in a Site.';
        ELSE
            -- Delete the region
            DELETE FROM region WHERE region.region_id = region_id;
        END IF;
    END IF;
END //
DELIMITER ;
/* Create stored procedure 'sp_delete_region' */

/* Create stored procedure 'sp_get_region' */
DROP PROCEDURE IF EXISTS sp_get_region;
DELIMITER //
CREATE PROCEDURE sp_get_region
(
    IN region_id INT
)
BEGIN
    -- Verify if the region exists
    IF NOT EXISTS (SELECT 1 FROM region WHERE region.region_id = region_id) THEN
        SIGNAL SQLSTATE '45002'
        SET MESSAGE_TEXT = '45002 - Region does not exist.';
    ELSE
        -- Get the region
        SELECT region_id, region_name FROM region WHERE region.region_id = region_id;
    END IF;
END //
DELIMITER ;
/* Create stored procedure 'sp_get_region' */

/* Create stored procedure 'sp_get_regions' */
DROP PROCEDURE IF EXISTS sp_get_regions;
DELIMITER //
CREATE PROCEDURE sp_get_regions()
BEGIN
    -- Get all regions
    SELECT region_id, region_name FROM region;
END //
DELIMITER ;
/* Create stored procedure 'sp_get_regions' */
/* Stored Procedures */