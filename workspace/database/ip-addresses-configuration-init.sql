/* Create 'ip_addresses_configuration' table */
DROP TABLE IF EXISTS ip_addresses_configuration;
CREATE TABLE ip_addresses_configuration (
    ip_address_id INT PRIMARY KEY AUTO_INCREMENT,
    fk_ip_address_interface INT NOT NULL,
    ip_address_alias VARCHAR(512) DEFAULT NULL,
    ip_address_state VARCHAR(8) DEFAULT NULL,
    ip_address VARCHAR(64) NOT NULL,
    ip_address_netmask VARCHAR(64) NOT NULL,
    ip_address_network VARCHAR(64) NOT NULL,
    ip_address_gateway VARCHAR(64) NOT NULL,
    FOREIGN KEY (fk_ip_address_interface) REFERENCES interface (interface_id)
);