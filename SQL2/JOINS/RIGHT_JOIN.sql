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

SELECT * FROM customers;
SELECT *FROM orders;


-- LEFT JOIN
SELECT *
FROM customers c
RIGHT JOIN orders o 
ON c.customer_id = o.customer_id;

-- RIGHT JOIN me similar values both tables ki print hoke aayegi but remaining values sirf RIGHT side ke tables mese hi print hogi
-- in short RIGHT table ki sari values rakhega and LEFT table ki sirf matching values