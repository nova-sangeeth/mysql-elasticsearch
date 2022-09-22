-- creating the database for instaqp admin and instaqp
CREATE DATABASE  instaqp CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci;

-- create users for instaqp and instaqp admin
CREATE USER 'instaqp'@'localhost' IDENTIFIED BY 'passw0rd';
CREATE USER 'instaqp'@'%' IDENTIFIED BY 'passw0rd';


-- giving permission to instaqp user account to the databases
GRANT ALL PRIVILEGES ON instaqp.* TO 'instaqp'@'%';

FLUSH PRIVILEGES;
