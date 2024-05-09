-- sql script that creates a table users.

CREATE TABLE IF NOT EXISTS users (
id int PRIMARY KEY NOT NULL,
email varchar(255) NOT NULL UNIQUE,

name varchar(255),
);
