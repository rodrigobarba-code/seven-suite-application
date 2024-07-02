/* Create 'interface' table */
DROP TABLE IF EXISTS interface;
CREATE TABLE interface (
    interface_id INT PRIMARY KEY AUTO_INCREMENT,
    fk_router_id INT,
    interface_state BOOLEAN,
    interface_name VARCHAR(256),
    interface_type VARCHAR(256),
    interface_mtu DOUBLE,
    FOREIGN KEY (fk_router_id) REFERENCES router (router_id)
);
/* Create 'interface' table */
