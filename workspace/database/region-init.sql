/* Create 'regions' table */
DROP TABLE IF EXISTS region;
CREATE TABLE region
(
    region_id INT PRIMARY KEY AUTO_INCREMENT,
    region_name VARCHAR(100) NOT NULL
);
/* Create 'regions' table */

/* Stored Procedures */

/* Create 'get_all_regions' stored procedure */
DROP PROCEDURE IF EXISTS sp_get_all_regions;
DELIMITER //
CREATE PROCEDURE sp_get_all_regions()
BEGIN
SELECT * FROM region;
END
// DELIMITER ;
/* Create 'get_all_regions' stored procedure */

/* Create 'get_region_by_id' stored procedure */
DROP PROCEDURE IF EXISTS sp_get_region_by_id;
DELIMITER //
CREATE PROCEDURE sp_get_region_by_id(IN region_id INT)
BEGIN
SELECT * FROM region WHERE region.region_id = region_id;
END
// DELIMITER ;
/* Create 'get_region_by_id' stored procedure */

/* Create 'add_region' stored procedure */
DROP PROCEDURE IF EXISTS sp_add_region;
DELIMITER //
CREATE PROCEDURE sp_add_region(IN region_name VARCHAR (100))
BEGIN
INSERT INTO region(region_name)
VALUES (region_name);
END
// DELIMITER ;
/* Create 'add_region' stored procedure */

/* Create 'update_region' stored procedure */
DROP PROCEDURE IF EXISTS sp_update_region;
DELIMITER //
CREATE PROCEDURE sp_update_region(IN region_id INT, IN region_name VARCHAR (100))
BEGIN
IF EXISTS (SELECT * FROM region WHERE region.region_id = region_id) THEN
UPDATE region
SET region.region_name = region_name
WHERE region.region_id = region_id;
ELSE
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = 'Region does not exist';
END IF;
END
// DELIMITER ;
/* Create 'update_region' stored procedure */

/* Create 'delete_region' stored procedure */
DROP PROCEDURE IF EXISTS sp_delete_region;
DELIMITER //
CREATE PROCEDURE sp_delete_region(IN region_id INT)
BEGIN
IF EXISTS (SELECT * FROM region WHERE region.region_id = region_id) THEN
DELETE FROM region WHERE region.region_id = region_id;
ELSE
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = 'Region does not exist';
END IF;
END
// DELIMITER ;
/* Create 'delete_region' stored procedure */

/* Stored Procedures */