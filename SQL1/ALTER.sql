CREATE DATABASE IF NOT EXISTS instagram;
USE instagram;

CREATE TABLE users (
   id INT,
   age INT,
   name VARCHAR(23) NOT NULL,
   email VARCHAR(50) UNIQUE,
   followers INT DEFAULT 0,
   following INT, 
   CONSTRAINT CHECK (age >= 13),
   PRIMARY KEY (id)
);

INSERT INTO users
(id, age, name, email, followers, following)
VALUES
(1, 14, "Shanku", "shanku@gmail.com", 123, 145),
(2, 15, "Kiki", "kiki@gmail.com", 533, 345),
(3, 16, "Pittu", "pittu@gmail.com", 453, 545),
(4, 17, "Kookie", "kookie@gmail.com", 343, 745);


-- ALTER is used to change the schema

-- ADD- add the colm
ALTER TABLE users
ADD COLUMN city VARCHAR(25) DEFAULT "Delhi";

-- DROP- delete the single colm only not whole table
ALTER TABLE users
DROP COLUMN age;

-- RENAME- rename the table name not colm name
ALTER TABLE users
RENAME TO instaUser;

-- CHANGE- change the colm name not table name 
ALTER TABLE users
CHANGE COLUMN followers subs INT DEFAULT 0;

-- MODIFY- modify the values
ALTER TABLE users
MODIFY subs INT DEFAULT 5;


-- Table ko view kiya
SELECT * FROM users;