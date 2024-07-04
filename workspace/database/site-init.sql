/* Create 'site' table */
DROP TABLE IF EXISTS site;
CREATE TABLE site (
    site_id INT PRIMARY KEY AUTO_INCREMENT,
    fk_region_id INT NOT NULL,
    site_name VARCHAR(100) NOT NULL,
    site_segment INT NOT NULL,
    FOREIGN KEY (fk_region_id) REFERENCES region (region_id)
);
/* Create 'site' table */

/* Create 'verify_region' stored procedure*/

DROP PROCEDURE IF EXISTS sp_verify_region;
DELIMITER //
CREATE PROCEDURE sp_verify_region(IN site_id INT)
BEGIN
SELECT region.region_name FROM region
JOIN site ON region.region_id = site.fk_region_id
WHERE site.site_id = site_id;
END
// DELIMITER ;
/* Create 'verify_region' stored procedure */

/* Create 'add_site' stored procedure*/

DROP PROCEDURE IF EXISTS sp_add_site;
DELIMITER //
CREATE PROCEDURE sp_add_site(IN fk_region_id INT, IN site_name VARCHAR(100), IN site_segment INT)
BEGIN
INSERT INTO site(fk_region_id, site_name, site_segment)
VALUES (fk_region_id, site_name, site_segment);
END
// DELIMITER ;
/* Create 'add_site' stored procedure */

/* Create 'get_all_sites' stored procedure*/

DROP PROCEDURE IF EXISTS sp_get_all_sites;
DELIMITER //
CREATE PROCEDURE sp_get_all_sites()
BEGIN
SELECT * FROM site;
END
// DELIMITER ;
/* Create 'get_all_sites' stored procedure */

/* Create 'get_site_by_id' */
DROP PROCEDURE IF EXISTS sp_get_site_by_id;
DELIMITER //
CREATE PROCEDURE `sp_get_site_by_id`(IN site_id INT)
BEGIN
SELECT * FROM site WHERE site.site_id = site_id;
END
// DELIMITER ;
/* Create 'get_site_by_id' stored procedure */

DROP PROCEDURE IF EXISTS sp_delete_site;
DELIMITER //
CREATE PROCEDURE sp_delete_site(IN site_id INT)
BEGIN
IF EXISTS (SELECT * FROM site WHERE site.site_id = site_id) THEN
DELETE FROM site WHERE site.site_id = site_id;
ELSE
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = 'Site does not exist';
END IF;
END
// DELIMITER ;
/* Create 'delete_site' stored procedure */

/* Create 'update_site' stored procedure by just asking the id of the site */
DROP PROCEDURE IF EXISTS sp_update_site;
DELIMITER //
CREATE PROCEDURE sp_update_site(IN site_id INT, IN fk_region_id INT, IN site_name VARCHAR(100), IN site_segment INT)
BEGIN
IF EXISTS (SELECT * FROM site WHERE site.site_id = site_id) THEN
UPDATE site
SET site.fk_region_id = fk_region_id, site.site_name = site_name, site.site_segment = site_segment
WHERE site.site_id = site_id;
ELSE
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = 'Site does not exist';
END IF;
END
// DELIMITER ;
/* Create 'update_site' stored procedure */
