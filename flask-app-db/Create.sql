CREATE DATABASE IF NOT EXISTS skyrim;
USE skyrimdb;
CREATE TABLE IF NOT EXISTS Characters (
    char_id INT AUTO_INCREMENT,
    name CHAR(20),
    race CHAR(20),
    archetype CHAR(50)
    PRIMARY KEY (char_id)
);