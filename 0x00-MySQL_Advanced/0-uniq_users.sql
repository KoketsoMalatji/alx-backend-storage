-- SQL script that creates a table users
CREATE TABLE if NOT EXISTS `users` (
       `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
       `email` VARCHAR(255) NOT NULL UNIQUE,
       `name`  VARCHAR(255)
);
