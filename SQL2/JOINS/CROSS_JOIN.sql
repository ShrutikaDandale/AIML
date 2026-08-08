USE prime;
CREATE TABLE customers (
customer_id INT PRIMARY KEY, 
name VARCHAR(50), 
city VARCHAR(50)
);

INSERT INTO customers 
VALUES
(1, 'Alice', 'Mumbai'),
(2, 'Bob', 'Delhi'),
(3, 'Charlie', 'Bangalore'),
(4, 'David', 'Mumbai');

CREATE TABLE orders (
order_id INT PRIMARY KEY,
customer_id INT,
amount INT
);

INSERT INTO orders
VALUES
(101, 1, 500),
(102, 1, 900),
(103, 2, 300),
(104, 5, 700);

-- CROSS JOIN
SELECT * 
FROM customers
CROSS JOIN orders;

-- in CROSS JOIN each row will be match with every other row in the another table
-- suppose we have alice in table A then alice will be join with  Alice 101, Alice 102, Alice 103, Alice 104 all of the values same with the eachothers
