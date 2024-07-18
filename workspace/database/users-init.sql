/* Create 'users' table, use bytes for the size of the table column (64,128,etc)*/
CREATE TABLE users
(
    user_id    INT          NOT NULL AUTO_INCREMENT,
    username   VARCHAR(128) NOT NULL,
    password   VARCHAR(128) NOT NULL,
    name       VARCHAR(128) NOT NULL,
    lastname   VARCHAR(128) NOT NULL,
    email      VARCHAR(128) NOT NULL,
    phone      VARCHAR(64)  NOT NULL,
    image      VARCHAR(128) NOT NULL,
    privileges enum('admin','user', 'guest') NOT NULL,
    state      enum('active','inactive') NOT NULL,
    PRIMARY KEY (user_id)
);

/* Create 'add_user' stored procedure, ignore the column 'state'*/
DROP PROCEDURE IF EXISTS sp_add_user;
DELIMITER
//
CREATE PROCEDURE sp_add_user(IN username VARCHAR (128), IN password VARCHAR (128), IN name VARCHAR (128),
                             IN lastname VARCHAR (128), IN email VARCHAR (128), IN phone VARCHAR (64),
                             IN image VARCHAR (128), IN privileges ENUM('admin', 'user', 'guest'))
BEGIN
INSERT INTO users(username, password, name, lastname, email, phone, image, privileges, state)
VALUES (username, password, name, lastname, email, phone, image, privileges, null);
END
// DELIMITER ;
/* Create 'add_user' stored procedure, ignore the column 'state'*/

/* Create 'get_all_users' stored procedure*/
DROP PROCEDURE IF EXISTS sp_get_all_users;
DELIMITER //
CREATE PROCEDURE sp_get_all_users()