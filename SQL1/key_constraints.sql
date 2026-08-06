-- PRIMARY KEY & FOREIGN KEY



-- humne pehele instagram nam ka DB banaya
CREATE DATABASE IF NOT EXISTS instagram;

-- fir us DB ko use kiya 
USE instagram;

-- instagram DB me table create kiya users ka
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


-- post table create kiya 
CREATE TABLE post (
   id INT PRIMARY KEY,
   content VARCHAR(100),
   user_id INT,
   FOREIGN KEY (user_id) REFERENCES users(id)
);

-- yaha users me primary key id hai & post ke table me primary key id hai and foreign key user_id hai