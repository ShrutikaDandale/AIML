USE prime;
CREATE TABLE bank_acc (
  account_id INT PRIMARY KEY,
  name varchar(50),
  balance DECIMAL(10, 2),
  branch VARCHAR(50)
);

INSERT INTO bank_acc VALUES
(1, 'Adam', 500.00, 'Mumbai'),
(2, 'Bob', 300.00, 'Delhi'),
(3, 'Charlie', 700.00, 'Banglore'),
(4, 'David', 1000.00, 'Noida');

SELECT * FROM bank_acc;


-- INDEX in sql
CREATE INDEX idx_branch ON bank_acc(branch);

SHOW INDEX FROM bank_acc;

SELECT *
FROM bank_acc
WHERE branch = "Mumbai";