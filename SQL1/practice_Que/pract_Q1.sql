CREATE DATABASE IF NOT EXISTS Collage;

USE Collage;

CREATE TABLE teacher(
 id INT,
 name VARCHAR(50),
 subject VARCHAR(50),
 salary FLOAT
);

INSERT INTO teacher
(id, name, subject, salary)
VALUES
(23, "Shrutika", "math", 50000),
(47, "Pritish", "physics", 60000),
(18, "Dewanshi", "bio", 45000),
(9, "Shravani", "chemistry", 75000);

SELECT salary
FROM teacher WHERE salary > 55000;

ALTER TABLE teacher
CHANGE COLUMN salary ctc INT;

UPDATE teacher
SET ctc = ctc + ctc * 0.25;

ALTER TABLE teacher
ADD COLUMN city VARCHAR(50) DEFAULT "Gurgaon";

ALTER TABLE teacher
DROP COLUMN ctc;

SELECT * FROM teacher;