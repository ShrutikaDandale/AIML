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

-- SUB QUERIES
-- suppose we wanna print the amount which are greater than the avg of amt of all customers
SELECT * 
FROM orders
WHERE amount > (
   SELECT AVG(amount)
   FROM orders
); 

-- another way with SELECT
-- suppose hume customer ka count of order print karana hai means cust 1 ne kitane order diye cust 3 ne kitane order place kiye similar with others 
SELECT name,
 (
   SELECT COUNT(*)
   FROM orders o
   WHERE o.customer_id = c.customer_id
  ) AS order_count
FROM customers c;  

-- another way with FROM
SELECT 
     summary.customer_id,
     summary.avg_amount
FROM
     (
        SELECT
              customer_id,
              AVG(amount) as avg_amount
           FROM orders
           GROUP BY customer_id
     )  as summary;   
