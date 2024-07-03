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