---------ASSIGNMENT----------
----BANKING SYSTEM----
---TASK 1---
Create database HMBank

Create table Customers(customer_id int Constraint pk_cust_id PRIMARY KEY, first_name VARCHAR(30), last_name VARCHAR(30), DOB date, email VARCHAR(100), phone_number int)
Alter table Customers add address varchar(100)
ALTER TABLE Customers alter COLUMN phone_number BIGINT;

select * from Customers


Create table Accounts(account_id int Constraint pk_acc_id PRIMARY KEY, customer_id int Constraint fk_cust_id FOREIGN KEY(customer_id) REFERENCES Customers(customer_id), account_type VARCHAR(50), balance int)

select * from Accounts


Create table Transactions(transaction_id int Constraint pk_trans_id PRIMARY KEY, account_id int Constraint fk_acc_id FOREIGN KEY(account_id) REFERENCES Accounts(account_id), transaction_type VARCHAR(50), amount int, transaction_date date)

select * from Transactions


Insert into Customers values(1, 'abc', 'xyz', '1990-01-01', 'abc@gmail.com', 1234567890, 'Chennai'),
(2, 'def', 'uvw', '1985-05-12', 'def@gmail.com', 2345678901, 'Mumbai'),
(3, 'ghi', 'rst', '1992-03-10', 'ghi@gmail.com', 3456789012, 'Delhi'),
(4, 'jkl', 'opq', '1988-07-18', 'jkl@gmail.com', 4567890123, 'Chennai'),
(5, 'mno', 'lmn', '1995-11-25', 'mno@gmail.com', 5678901234, 'Kolkata'),
(6, 'pqr', 'ijk', '1991-09-09', 'pqr@gmail.com', 6789012345, 'Delhi');

Insert into Accounts values (101, 1, 'savings', 5000),
(102, 2, 'current', 1200),
(103, 3, 'savings', 0),
(104, 4, 'current', 2500),
(105, 5, 'savings', 800),
(106, 6, 'current', 1100)

Insert into Transactions values (201, 101, 'deposit', 2000, '2024-01-01'),
(202, 101, 'withdraw', 2000, '2024-02-01'),
(203, 102, 'deposit', 1200, '2024-01-15'),
(204, 104, 'withdraw', 1000, '2024-03-10'),
(205, 105, 'deposit', 800, '2024-04-01'),
(206, 106, 'deposit', 1100, '2024-05-01')

---TASK 2---
--1) Write a SQL query to retrieve the name, account type and email of all customers
Select c.first_name, c.last_name, a.account_type, c.email 
from Customers c 
INNER JOIN Accounts a 
ON c.customer_id=a.customer_id;

select * from Customers
select * from Accounts
select * from Transactions

--2) Write a SQL query to list all transaction corresponding customer
SELECT c.first_name, c.last_name, t.transaction_id, t.transaction_type, t.amount, t.transaction_date 
FROM Customers c 
INNER JOIN Accounts a 
ON c.customer_id = a.customer_id 
INNER JOIN Transactions t 
ON a.account_id = t.account_id;

--3) Write a SQL query to Combine first and last names of customers as a full_name
UPDATE Accounts SET balance = balance + 1000 WHERE account_id = 101;

--4) Combine first and last names as full_name
--select upper (first_name) from customers
--select upper (last_name) from customers
SELECT first_name + ' '+ last_name AS full_name FROM Customers;

--5) Remove savings accounts with balance = 0
DELETE FROM Accounts WHERE account_type = 'savings' AND balance = 0;

--6) Customers in specific city
SELECT * FROM Customers WHERE address = 'Chennai';

--7) Write a SQL query to Get the account balance for a specific account
SELECT balance FROM Accounts WHERE account_id = 104;

--8) Current accounts with balance > 1000
SELECT * FROM Accounts WHERE account_type = 'current' AND balance > 1000;

--9) Write a SQL query to Retrieve all transactions for a specific account
SELECT * FROM Transactions WHERE account_id = 101;

--10) Write a SQL query to Calculate the interest accrued on savings accounts based on a given interest rate
SELECT account_id, balance, balance * 0.05 AS interest FROM Accounts WHERE account_type = 'savings';

--11) Accounts with balance less than overdraft limit
SELECT * FROM Accounts WHERE balance < 1000;

--12) Customers not in a specific city
SELECT * FROM Customers WHERE address != 'Delhi';

---TASK 3---
--1) Find the average account balance for all customers
Select AVG(balance) as avg_balance From Accounts;

--2) Retrieve the top 10 highest account balances
Select TOP 10 * from Accounts ORDER BY balance desc;

--3) Write a SQL query to Calculate Total Deposits for All Customers in specific date
Select SUM(amount) as total_deposit from Transactions where transaction_type = 'deposit' AND transaction_date = '2024-01-01';

--4) Write a SQL query to Find the Oldest and Newest Customers
-- Oldest customer
Select TOP 1 * from Customers ORDER BY DOB;

-- Newest customer
Select TOP 1 * from Customers ORDER BY DOB desc;

--5) Retrieve transaction details along with the account type
Select t.transaction_id, t.account_id, a.account_type, t.transaction_type, t.amount, t.transaction_date 
from Transactions t
INNER JOIN Accounts a 
ON t.account_id = a.account_id;

--6) Get a list of customers along with their account details
Select c.customer_id, c.first_name, c.last_name, a.account_id, a.account_type, a.balance
from Customers c
INNER JOIN Accounts a 
ON c.customer_id = a.customer_id;

--7) Retrieve transaction details along with customer information for a specific account
Select a.account_id, t.transaction_id, t.transaction_type, t.amount, t.transaction_date, c.customer_id, c.first_name, c.last_name, a.account_type
from Transactions t
INNER JOIN Accounts a 
ON t.account_id = a.account_id
INNER JOIN Customers c 
ON a.customer_id = c.customer_id
where t.account_id = 101;

--8) Identify customers who have more than one account
Select c.customer_id, c.first_name, c.last_name, 
COUNT(a.account_id) as account_count
from Customers c
INNER JOIN Accounts a
ON c.customer_id = a.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
having COUNT(a.account_id) > 1;

--9) Calculate the difference in transaction amounts between deposits and withdrawals
Select
(Select SUM(amount) from Transactions where transaction_type = 'deposit') -
(Select SUM(amount) from Transactions where transaction_type = 'withdraw') --subtracting 
as difference;

--10) Calculate the average daily balance for each account over a specified period
Select a.account_id, a.account_type,
       ISNULL(d.total_deposit, 0) - ISNULL(w.total_withdraw, 0) as net_change, --Net change=Total deposits - Total withdrawals
       ROUND((ISNULL(d.total_deposit, 0) - ISNULL(w.total_withdraw, 0)) / 120.0, 2) as avg_daily_change --1)Average daily change = Net change ÷ 120 days (from Jan 1 to Apr 30) --2) ISNULL(..., 0): If there's no deposit/withdraw, treat it as 0 --3) ROUND(..., 2):Round the result to 2 decimal places.
from Accounts a
LEFT JOIN (
    select account_id, SUM(amount) as total_deposit
    from Transactions
    where transaction_type = 'deposit'
      AND transaction_date BETWEEN '2024-01-01' AND '2024-04-30'
    GROUP BY account_id) d 
ON a.account_id = d.account_id
LEFT JOIN (
    Select account_id, SUM(amount) as total_withdraw
    from Transactions
    where transaction_type = 'withdraw'
      AND transaction_date BETWEEN '2024-01-01' AND '2024-04-30'
    GROUP BY account_id) w 
ON a.account_id = w.account_id;

--11) Calculate the total balance for each account type
Select account_type, SUM(balance) as total_balance
from Accounts
GROUP BY account_type;

--12) Identify accounts with the highest number of transactions (ordered descending)
Select account_id, COUNT(*) as t_count
from Transactions 
GROUP BY account_id
ORDER BY t_count desc;

--13) List customers with high aggregate account balances, along with their account types
Select c.customer_id, c.first_name, c.last_name, a.account_type, a.balance
from Customers c
INNER JOIN Accounts a 
ON c.customer_id = a.customer_id
where a.balance > 2000;

--14) Identify and list duplicate transactions based on amount, date, and account
Select account_id, amount, transaction_date, 
COUNT(*) as dup_trans
from Transactions
GROUP BY account_id, amount, transaction_date
having COUNT(*) > 1;

---TASK 4---
--1) Retrieve the customers with the highest account balance
Select c.customer_id, c.first_name, c.last_name, a.balance
from Customers c
INNER JOIN Accounts a 
ON c.customer_id = a.customer_id
where a.balance = 
    (select MAX(balance) from Accounts);

--2) Calculate the average account balance for customers who have more than one account
Select AVG(balance) as avg_balance
from Accounts
where customer_id IN 
    (select customer_id
     from Accounts
     GROUP BY customer_id
     having COUNT(*) > 1);

--3) Retrieve accounts with transactions whose amounts exceed the average transaction amount
Select *
from Transactions
where amount > 
    (Select AVG(amount) 
     from Transactions);

--4) Identify customers who have no recorded transactions
Select c.customer_id, c.first_name, c.last_name
from Customers c
where c.customer_id NOT IN 
    (select a.customer_id
     from Accounts a
     INNER JOIN Transactions t 
     ON a.account_id = t.account_id);

--5) Calculate the total balance of accounts with no recorded transactions
Select SUM(a.balance) as total_balance
from Accounts a
where a.account_id NOT IN 
    (Select t.account_id
     from Accounts a2
     INNER JOIN Transactions t 
     ON a2.account_id = t.account_id);

INSERT INTO Accounts VALUES (107, 3, 'savings', 0)
select * from accounts
INSERT INTO Transactions VALUES (207, 107, 'deposit', 500, '2024-06-15');

--6) Retrieve transactions for accounts with the lowest balance
SELECT * 
FROM Transactions 
WHERE account_id IN 
    (SELECT account_id 
     FROM Accounts 
     WHERE balance = (SELECT MIN(balance) FROM Accounts));

--7) Identify customers who have accounts of multiple types
Select a1.customer_id
from Accounts a1
INNER JOIN Accounts a2 
ON a1.customer_id = a2.customer_id AND a1.account_type <> a2.account_type
GROUP BY a1.customer_id;

--8) Calculate the percentage of each account type out of the total number of accounts
select account_type,
       COUNT(*) as count,
       ROUND(100.0 * COUNT(*) / (select COUNT(*) from Accounts), 2) as percentage
from Accounts
GROUP BY account_type;

--9) Retrieve all transactions for a customer with a given customer_id
Select *
from Transactions t
INNER JOIN Accounts a 
ON t.account_id = a.account_id
where a.customer_id = 3;

--10) Calculate the total balance for each account type, including a subquery in the SELECT clause
Select account_type,
SUM(balance) as total_balance,
    (Select SUM(balance) from Accounts) as overall_balance
from Accounts
GROUP BY account_type;