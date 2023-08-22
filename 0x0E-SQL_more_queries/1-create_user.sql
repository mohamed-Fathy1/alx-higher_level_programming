-- Write a script that creates the MySQL server user user_0d_1.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* FOR 'user_0d_1'@'localhost' WITH GRANT OPTION;
