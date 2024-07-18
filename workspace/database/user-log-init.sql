/* Create 'users_log' table, use bytes for the size of the table column (64,128,etc)*/
CREATE TABLE users_log
(
    user_log_id INT NOT NULL AUTO_INCREMENT,
    fk_user_id  INT NOT NULL,
    session_start TIMESTAMP NOT NULL,
    session_end TIMESTAMP NOT NULL,
    user_ip VARCHAR(64) NOT NULL,
    device VARCHAR(64) NOT NULL,
    log_action  ENUM('auth', 'logout', 'insert', 'update', 'delete') NOT NULL,
    PRIMARY KEY (user_log_id),
    FOREIGN KEY (fk_user_id) REFERENCES users (user_id)
);

/* Create a trigger for the 'users_log' table for generate a binnacle when a user logins and logout, insert, update, delete on the app */
DROP TRIGGER IF EXISTS tr_users_log;
DELIMITER //
CREATE TRIGGER tr_users_log
AFTER INSERT ON users
FOR EACH ROW
BEGIN
    INSERT INTO users_log(fk_user_id, session_start, session_end, user_ip, device, log_action)
    VALUES (NEW.user_id, NOW(), NOW(), ' ', ' ', 'insert');
END
//
DELIMITER ;

DROP TRIGGER IF EXISTS tr_users_log_update;
DELIMITER //
CREATE TRIGGER tr_users_log_update
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    INSERT INTO users_log(fk_user_id, session_start, session_end, user_ip, device, log_action)
    VALUES (NEW.user_id, NOW(), NOW(), ' ', ' ', 'update');
END
//
DELIMITER ;

DROP TRIGGER IF EXISTS tr_users_log_delete;
DELIMITER //
CREATE TRIGGER tr_users_log_delete
AFTER DELETE ON users
FOR EACH ROW
BEGIN
    INSERT INTO users_log(fk_user_id, session_start, session_end, user_ip, device, log_action)
    VALUES (OLD.user_id, NOW(), NOW(), ' ', ' ', 'delete');
END
//
DELIMITER ;

DROP TRIGGER IF EXISTS tr_users_log_login;
DELIMITER //
CREATE TRIGGER tr_users_log_login
AFTER INSERT ON users_log
FOR EACH ROW
BEGIN
    IF NEW.log_action = 'auth' THEN
        UPDATE users_log
        SET session_start = NOW()
        WHERE fk_user_id = NEW.fk_user_id AND log_action = 'auth' AND session_end = NEW.session_start;
    END IF;
END
//
DELIMITER ;

DROP TRIGGER IF EXISTS tr_users_log_logout;
DELIMITER //
CREATE TRIGGER tr_users_log_logout
AFTER INSERT ON users_log
FOR EACH ROW
BEGIN
    IF NEW.log_action = 'logout' THEN
        UPDATE users_log
        SET session_end = NOW()
        WHERE fk_user_id = NEW.fk_user_id AND log_action = 'logout' AND session_end = NEW.session_start;
    END IF;
END
//
DELIMITER ;

DROP TRIGGER IF EXISTS tr_users_log_insert;
DELIMITER //
CREATE TRIGGER tr_users_log_insert
AFTER INSERT ON users_log
FOR EACH ROW
BEGIN
    IF NEW.log_action = 'insert' THEN
        UPDATE users_log
        SET session_end = NOW()
        WHERE fk_user_id = NEW.fk_user_id AND log_action = 'insert' AND session_end = NEW.session_start;
    END IF;
END
//
DELIMITER ;

DROP TRIGGER IF EXISTS tr_users_log_update;
DELIMITER //
CREATE TRIGGER tr_users_log_update
AFTER INSERT ON users_log
FOR EACH ROW
BEGIN
    IF NEW.log_action = 'update' THEN
        UPDATE users_log
        SET session_end = NOW()
        WHERE fk_user_id = NEW.fk_user_id AND log_action = 'update' AND session_end = NEW.session_start;
    END IF;
END
//
DELIMITER ;

DROP TRIGGER IF EXISTS tr_users_log_delete;
DELIMITER //
CREATE TRIGGER tr_users_log_delete
AFTER INSERT ON users_log
FOR EACH ROW
BEGIN
    IF NEW.log_action = 'delete' THEN
        UPDATE users_log
        SET session_end = NOW()
        WHERE fk_user_id = NEW.fk_user_id AND log_action = 'delete' AND session_end = NEW.session_start;
    END IF;
END
//
DELIMITER ;
