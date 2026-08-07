-- Create Database
CREATE DATABASE IF NOT EXISTS Employee;

-- Use Database
USE Employee;

-- Delete table if it already exists (Optional)
DROP TABLE IF EXISTS emp_detail;

-- Create Table
CREATE TABLE emp_detail (
    EmpID INT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Department VARCHAR(50) NOT NULL,
    Salary INT NOT NULL,
    HireDate DATE NOT NULL
);

-- Insert Records
INSERT INTO emp_detail
(EmpID, FirstName, LastName, Department, Salary, HireDate)
VALUES
(101, 'Alice', 'Johnson', 'IT', 6500, '2020-03-15'),
(102, 'Mark', 'Rivera', 'HR', 4800, '2019-07-22'),
(103, 'Sophia', 'Lee', 'Finance', 7200, '2021-01-10'),
(104, 'Daniel', 'Kim', 'IT', 5800, '2018-11-05'),
(105, 'Emma', 'Brown', 'Marketing', 5300, '2022-04-18'),
(106, 'Liam', 'Patel', 'Finance', 6900, '2020-09-29'),
(107, 'Olivia', 'Garcia', 'HR', 4600, '2017-06-30'),
(108, 'Noah', 'Thompson', 'IT', 7500, '2023-02-12'),
(109, 'Ava', 'Martinez', 'Marketing', 5100, '2019-12-02'),
(110, 'Ethan', 'Davis', 'Finance', 8000, '2016-05-14');

-- Q1. Write a query to display every employee and all their data.
SELECT * FROM emp_detail;

-- Q2. List only the FirstName, LastName, and Salary of every employee
SELECT FirstName, LastName, Salary
FROM emp_detail;

-- Q3. Show all employees who work in the 'IT' department.
SELECT FirstName
FROM emp_detail
WHERE Department = 'IT';

-- Q4. Retrieve employees with a salary greater than 6000.
SELECT *
FROM emp_detail
WHERE salary > 6000;

-- Q5. List all employees ordered by HireDate from newest to oldest.
SELECT *
FROM emp_detail 
ORDER BY HireDate ASC;

-- Q6. Show a list of all unique departments present in the table
SELECT DISTINCT Department 
FROM emp_detail;

-- Q7. Find employees whose first name starts with ‘Aʼ
SELECT FirstName
FROM emp_detail 
WHERE FirstName LIKE 'A%';

-- 'A%'     → starts with A
-- '%A'     → ends with A
-- '%A%'    → contains A anywhere  

-- Q8. Show employees whose salaries are between 4000 and 7000.
SELECT * 
FROM emp_detail
WHERE salary BETWEEN 4000 and 7000;

-- Q9. Find the average salary of all employees
SELECT avg(salary)
FROM emp_detail;

-- Q10. List each department along with the number of employees, but only include departmentswith more than 3 employees
SELECT Department, COUNT(Department) AS EmployeeCount
FROM emp_detail
GROUP BY Department
HAVING COUNT(Department) > 3;