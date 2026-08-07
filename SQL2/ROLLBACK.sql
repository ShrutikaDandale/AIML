CREATE DATABASE IF NOT EXISTS prime;

USE prime;

DROP TABLE IF EXISTS accounts;

CREATE TABLE accounts (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    balance DECIMAL(10,2)
);

INSERT INTO accounts (id, name, balance)
VALUES
(1, 'Shrutika', 50000.00),
(2, 'Pritish', 1000.00),
(3, 'Prachi', 30000.00);

-- Check Initial Data
SELECT * FROM accounts;


-- TRANSACTION

START TRANSACTION;

-- Transfer ₹50 from Shrutika(id 1) to Pritish(id 2)
UPDATE accounts
SET balance = balance - 50
WHERE id = 1;

COMMIT;

UPDATE accounts 
SET balance = balance + 50
WHERE id = 2;

ROLLBACK;


-- Check Updated Data
SELECT * FROM accounts;