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


-- Frequently used operators
SELECT name, followers, age
FROM users

 WHERE followers >= 200 AND age >= 13; --AND

WHERE followers >= 200 OR age >= 13; --OR

WHERE age BETWEEN 13 and 20; --BETWEEN

WHERE email IN ("shanku@gmail.com", "kiki@gmail.com", "pittu@gmail.com", "kookie@gmail.com"); --IN

WHERE age NOT IN (13, 20); --NOT IN