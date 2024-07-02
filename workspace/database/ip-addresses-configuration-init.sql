/* Create 'ip_addresses_configuration' table */
DROP TABLE IF EXISTS ip_addresses_configuration;
CREATE TABLE ip_addresses_configuration (
    ip_address_id INT PRIMARY KEY AUTO_INCREMENT,
    fk_ip_address_interface INT,
    ip_address_alias VARCHAR(512),
    ip_address_state VARCHAR(64),
    ip_address VARCHAR(64),
    ip_address_netmask VARCHAR(64),
    ip_address_network VARCHAR(64),
    ip_address_gateway VARCHAR(64),
    FOREIGN KEY (fk_ip_address_interface) REFERENCES interface (interface_id)
);