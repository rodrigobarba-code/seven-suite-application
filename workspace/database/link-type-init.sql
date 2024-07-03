/* Create 'link_type' table */
DROP TABLE IF EXISTS link_type;
CREATE TABLE link_type (
    link_type_id INT PRIMARY KEY AUTO_INCREMENT,
    link_type_name VARCHAR(100) NOT NULL,
    link_type_description VARCHAR(512) NOT NULL,
    link_type_segment INT NOT NULL
);
/* Create 'link_type' table */
