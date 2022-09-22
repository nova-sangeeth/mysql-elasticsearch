-- creating the database for instaqp admin and instaqp
CREATE DATABASE instaqp CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci;
-- create users for instaqp and instaqp admin
CREATE USER 'instaqp' @'localhost' IDENTIFIED BY 'passw0rd';
CREATE USER 'instaqp' @'%' IDENTIFIED BY 'passw0rd';
-- giving permission to instaqp user account to the databases
GRANT ALL PRIVILEGES ON instaqp.* TO 'instaqp' @'%';

FLUSH PRIVILEGES;

-- CREATE TABLE es_table (
--     id BIGINT(20) UNSIGNED NOT NULL,
--     PRIMARY KEY (id),
--     UNIQUE KEY unique_id (id),
--     client_name VARCHAR(32) NOT NULL,
--     modification_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
-- );
-- CREATE TABLE es_table_2 (
--     id BIGINT(20) UNSIGNED NOT NULL,
--     PRIMARY KEY (id),
--     UNIQUE KEY unique_id (id),
--     client_name VARCHAR(32) NOT NULL,
--     modification_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
-- );
-- CREATE TABLE es_table_3 (
--     id BIGINT(20) UNSIGNED NOT NULL,
--     PRIMARY KEY (id),
--     UNIQUE KEY unique_id (id),
--     client_name VARCHAR(32) NOT NULL,
--     modification_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
-- );

-- INSERT INTO es_table (id, client_name)
-- VALUES (1, "test one"),
--     (2, "test two"),
--     (3, "test three"),
--     (4, "test four"),
--     (5, "new test five"),
--     (6, "test six"),
--     (7, "test seven");
-- INSERT INTO es_table_2 (id, client_name)
-- VALUES (1, "test one"),
--     (2, "test two"),
--     (3, "test three"),
--     (4, "test four"),
--     (5, "new test five"),
--     (6, "test six"),
--     (7, "test seven");
-- INSERT INTO es_table_3 (id, client_name)
-- VALUES (1, "test one"),
--     (2, "test two"),
--     (3, "test three"),
--     (4, "test four"),
--     (5, "new test five"),
--     (6, "test six"),
--     (7, "test seven");