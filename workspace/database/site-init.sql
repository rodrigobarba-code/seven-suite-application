/* Create 'site' table */
DROP TABLE IF EXISTS site;
CREATE TABLE site (
    site_id INT PRIMARY KEY AUTO_INCREMENT,
    fk_region_id INT,
    site_name VARCHAR(100),
    FOREIGN KEY (fk_region_id) REFERENCES region (region_id)
);
/* Create 'site' table */