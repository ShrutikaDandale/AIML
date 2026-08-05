-- humne pehele instagram nam ka DB banaya
CREATE DATABASE IF NOT EXISTS instagram;

-- fir us DB ko use kiya 
USE instagram;

-- instagfram DB me table create kiya users karake
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

 
-- users tablr me following data insert kiya
INSERT INTO users
(id, age, name, email, followers, following)
VALUES
(1, 14, "Shanku", "shanku@gmail.com", 123, 145),
(2, 15, "Kiki", "kiki@gmail.com", 533, 345),
(3, 16, "Pittu", "pittu@gmail.com", 453, 545),
(4, 17, "Kookie", "kookie@gmail.com", 343, 745);

-- post table create kiya 
CREATE TABLE post (
   id INT PRIMARY KEY,
   content VARCHAR(100),
   user_id INT,
   FOREIGN KEY (user_id) REFERENCES users(id)
);