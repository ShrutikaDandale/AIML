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


-- Stored procedure - it is a predefine set of SQL statements that you can save in the DB and execute whenever needed
DELIMITER $$ -- we dont want to terminate our program at semicolon ; cause it comes inside the procedure but writing it is also imp to not get syntax error so that we will terminate it using the delimiter $$ symbol 

CREATE PROCEDURE check_balance(IN acc_id INT)
BEGIN
      SELECT balance 
      FROM bank_acc
      WHERE account_id = acc_id;
END $$

DELIMITER ;   -- set delimiter back to semicolon for next opretion


-- call the procedure
CALL check_balance(1, @balance);
SELECT @balance;

DROP PROCEDURE IF EXISTS 