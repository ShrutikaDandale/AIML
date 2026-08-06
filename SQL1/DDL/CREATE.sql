-- humne instagram DB create kiya 
CREATE DATABASE IF NOT EXISTS instagram;

-- us instagram DB ko use kiya
USE instagram;

-- instagram DB me table create kiya user name ka
CREATE TABLE user (
   id INT,
   name VARCHAR(30) NOT NULL,
   email VARCHAR(50),
   followers INT DEFAULT 0,
   following INT
);

