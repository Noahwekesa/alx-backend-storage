-- sql script that creates a table users.

CREATE TABLE IF NOT EXISTS users (
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  email varchar(255) NOT NULL UNIQUE,
  name varchar(255)
);
