/* Create 'interface' table */
DROP TABLE IF EXISTS interface;
CREATE TABLE interface (
    interface_id INT PRIMARY KEY AUTO_INCREMENT,
    fk_router_id VARCHAR(512) NOT NULL,
    interface_state BOOLEAN DEFAULT FALSE,
    interface_name VARCHAR(256) NULL,
    interface_type VARCHAR(256) NOT NULL,
    interface_mtu DOUBLE NULL,
    FOREIGN KEY (fk_router_id) REFERENCES router (router_id)
);
/* Create 'interface' table */
