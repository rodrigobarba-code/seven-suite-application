/* Create 'router' table */
DROP TABLE IF EXISTS router;
CREATE TABLE router (
    router_id VARCHAR(10240) NOT NULL PRIMARY KEY,
    router_name VARCHAR(256) NULL,
    fk_site_id INT NOT NULL,
    fk_session_id INT NULL,
    fk_ip_address_id INT NULL
);
/* Create 'router' table */

/* Alter table 'router' to include foreign keys */
ALTER TABLE router
ADD FOREIGN KEY (fk_site_id) REFERENCES site(site_id),
ADD FOREIGN KEY (fk_session_id) REFERENCES session_information(session_id),
ADD FOREIGN KEY (fk_ip_address_id) REFERENCES ip_addresses_configuration(ip_address_id);
/* Alter table 'router' to include foreign keys */

