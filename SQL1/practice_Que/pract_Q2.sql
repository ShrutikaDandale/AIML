CREATE TABLE student_info(
 roll_no INT PRIMARY KEY,
 name VARCHAR(50),
 city VARCHAR(50),
 marks INT
);

INSERT INTO student_info
(roll_no, name, city, marks)
VALUES
(101, "RM", "Skorea", 76),
(108, "Jin", "Busan", 32),
(112, "Jhope", "Degue", 45),
(124, "Suga", "Seoul", 80);

SELECT marks
FROM student_info WHERE marks > 75;

SELECT DISTINCT city
FROM student_info;

SELECT city, max(marks)
FROM student_info
GROUP BY city;

SELECT avg(marks)
FROM student_info;

ALTER TABLE student_info
ADD COLUMN grade VARCHAR(2);

UPDATE student_info
SET grade = "O"
WHERE marks >= 80;

UPDATE student_info
SET grade = "A"
WHERE marks >= 70 AND marks < 80;

UPDATE student_info
SET grade = "B"
WHERE marks <= 60 AND marks <70;

SELECT * FROM student_info