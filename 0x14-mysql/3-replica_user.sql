-- 1-replica_user.sql
-- creates the MySQL server user replica_user
CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'replica280';
-- Grants permission to replicate primary mysql server
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
-- grants permission to check replica_user is created with right permissions
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
