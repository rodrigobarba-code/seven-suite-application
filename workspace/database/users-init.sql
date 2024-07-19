/* Create 'users' table, use bytes for the size of the table column (64,128,etc)*/
CREATE TABLE users
(
    user_id    INT          NOT NULL AUTO_INCREMENT,
    user_username   VARCHAR(128) NOT NULL,
    user_password   VARCHAR(128) NOT NULL,
    user_name       VARCHAR(128) NOT NULL,
    user_lastname   VARCHAR(128) NOT NULL,
    privileges enum('admin','user', 'guest') NOT NULL,
    state      enum('active','inactive') NOT NULL,
    PRIMARY KEY (user_id)
);

/* Create 'add_user' stored procedure, ignore the column 'state'*/
DELIMITER //
CREATE PROCEDURE add_user(
    IN user_username VARCHAR(128),
    IN user_password VARCHAR(128),
    IN user_name     VARCHAR(128),
    IN user_lastname VARCHAR(128),
    IN privileges    ENUM('admin', 'user', 'guest')
)
BEGIN
    INSERT INTO users(user_username, user_password, user_name, user_lastname, privileges, state)
    VALUES (user_username, user_password, user_name, user_lastname, privileges, 'active');
END
//
DELIMITER ;

/* Create 'update_user' stored procedure, ignore the column 'state'*/
DELIMITER //
CREATE PROCEDURE sp_update_user(
    IN user_id       INT,
    IN user_username VARCHAR(128),
    IN user_password VARCHAR(128),
    IN user_name     VARCHAR(128),
    IN user_lastname VARCHAR(128),
    IN privileges    ENUM('admin', 'user', 'guest')
)
BEGIN
    UPDATE users
    SET user_username = user_username,
        user_password = user_password,
        user_name = user_name,
        user_lastname = user_lastname,
        privileges = privileges
    WHERE user_id = user_id;
END
//
DELIMITER ;

/* Create 'delete_user' stored procedure, ignore the column 'state'*/
DELIMITER //
CREATE PROCEDURE sp_delete_user(
    IN user_id INT
)
BEGIN
    DELETE FROM users
    WHERE user_id = user_id;
END
//
DELIMITER ;

/* Create 'get_user' stored procedure, ignore the column 'state'*/
DELIMITER //
CREATE PROCEDURE sp_get_user(
    IN user_id INT
)
BEGIN
    SELECT user_id, user_username, user_name, user_lastname, privileges
    FROM users
    WHERE user_id = user_id;
END
//
DELIMITER ;

/* Create 'get_users' stored procedure, ignore the column 'state'*/
DELIMITER //
CREATE PROCEDURE sp_get_users()
BEGIN
    SELECT user_id, user_username, user_name, user_lastname, privileges
    FROM users;
END
//
DELIMITER ;

/* Create 'get_users_by_privileges' stored procedure, ignore the column 'state'*/
DELIMITER //
CREATE PROCEDURE sp_get_users_by_privileges(
    IN privileges ENUM('admin', 'user', 'guest ')
)
BEGIN
    SELECT user_id, user_username, user_name, user_lastname, privileges
    FROM users
    WHERE privileges = privileges;
END
//
DELIMITER ;

/* Create 'get_users_by_state' stored procedure, ignore the column 'state'*/
DELIMITER //
CREATE PROCEDURE sp_get_users_by_state(
    IN state ENUM('active', 'inactive')
)
BEGIN
    SELECT user_id, user_username, user_name, user_lastname, privileges
    FROM users
    WHERE state = state;
END
//
DELIMITER ;

/* Create 'get_users_by_privileges_and_state' stored procedure, ignore the column 'state'*/
DELIMITER //
CREATE PROCEDURE sp_get_users_by_privileges_and_state(
    IN privileges ENUM('admin', 'user', 'guest'),
    IN state ENUM('active', 'inactive')
)
BEGIN
    SELECT user_id, user_username, user_name, user_lastname, privileges
    FROM users
    WHERE privileges = privileges AND state = state;
END
//
DELIMITER ;

/* Create 'get_users_by_name' stored procedure, ignore the column 'state'*/
DELIMITER //
CREATE PROCEDURE sp_get_users_by_name(
    IN user_name VARCHAR(128)
)
BEGIN
    SELECT user_id, user_username, user_name, user_lastname, privileges
    FROM users
    WHERE user_name = user_name;
END
//
DELIMITER ;

/* Create 'get_users_by_lastname' stored procedure, ignore the column 'state'*/
DELIMITER //
CREATE PROCEDURE sp_get_users_by_lastname(
    IN user_lastname VARCHAR(128)
)
BEGIN
    SELECT user_id, user_username, user_name, user_lastname, privileges
    FROM users
    WHERE user_lastname = user_lastname;
END
//
DELIMITER ;