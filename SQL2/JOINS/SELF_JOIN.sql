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

-- SELF JOIN
SELECT * 
FROM customers as A
JOIN customers as B
ON A.customer_id = B.customer_id;

-- SELF JOIN is basically used with the same table like the copy of the same table the table is join with itself
-- humare data me jaha kaha bhi same same id repeated hue hogi self join unhe join karane ka kam karata hai