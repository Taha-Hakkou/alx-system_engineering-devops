-- 1-tyrell_corp_db.sql
-- creates the database tyrell_corp in your MySQL server if doesn't exist
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
-- creates a table called nexus6 in the current database in your MySQL server
CREATE TABLE nexus6(
id INT,
name VARCHAR(256)
);
INSERT INTO nexus6 VALUES (1, 'Leon');
-- grant select permissions on the table
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
