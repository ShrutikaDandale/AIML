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


-- GROUP BY clause is used to grp the elements, here age ke basis pe grp pade hai and jinka age same hai unhe ek grp me dala gaya hai 
SELECT age, count(id)
FROM users 
GROUP BY age;

-- suppose 2 logo ka age 14 hai to vo ek grp me hoge and count(id) 2 hoga
