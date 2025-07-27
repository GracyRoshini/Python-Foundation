-------------CASE STUDY--------------------

-------E COMMERCE---------

--DATABASE
Create database Ecommerce

--TABLES
Create table customers(customer_id int Identity(1,1) Constraint pk_cid PRIMARY KEY, 
name VARCHAR(50), 
email VARCHAR(50), 
password VARCHAR(50))

Create table products (product_id int Identity(1,1) Constraint pk_pid PRIMARY KEY, 
name VARCHAR(50), 
price int, 
description VARCHAR(100), 
stockQuantity int)

Create table cart (cart_id int Identity(1,1) Constraint pk_cartid PRIMARY KEY, 
customer_id int Constraint fk_cid FOREIGN KEY(customer_id) REFERENCES customers(customer_id), 
product_id int CONSTRAINT fk_pid FOREIGN KEY(product_id) REFERENCES products(product_id), 
quantity int)

Create table orders (order_id int Identity(1,1) CONSTRAINT pk_oid PRIMARY KEY, 
customer_id int CONSTRAINT fk2_cid FOREIGN KEY (customer_id) REFERENCES customers(customer_id), 
order_date date, 
total_price int, 
shipping_address VARCHAR(100))

Create table order_items (order_item_id int Identity(1,1) CONSTRAINT pk_order_item_id PRIMARY KEY, 
order_id int CONSTRAINT fk_oid FOREIGN KEY(order_id) REFERENCES orders(order_id), 
product_id int CONSTRAINT fk2_pid FOREIGN KEY(product_id) REFERENCES products(product_id), 
quantity int)

--TO DISPLAY TABLE STRUCTURES
select * from customers
select * from products
select * from cart
select * from orders
select * from order_items

--TO INSERT VALUES INTO TABLES
Insert into customers values (1, 'Abc', 'abc@gmail.com', 'pass1'), 
(2, 'Def', 'def@gmail.com', 'pass2'), 
(3, 'Ghi', 'Ghi@gmail.com', 'pass3'), 
(4, 'Jkl', 'jkl@gmail.com', 'pass4'), 
(5, 'Mno', 'mno@gmail.com', 'pass5'), 
(6, 'Pqr', 'pqr@gmail.com', 'pass6');

Insert into products values (1, 'Printer', 4202, 'All-in-one', 36), 
(2, 'Camera', 4234, 'Digital SLR', 26), 
(3, 'Headphones', 4688, 'Noise cancelling', 7), 
(4, 'Tablet', 4731, 'Portable device', 24),
(5, 'Laptop', 1206, 'High-end device', 17), 
(6, 'Phone', 1144, 'Smart gadget', 22);

Insert into cart values (1, 1, 1, 1), (2, 2, 2, 2), (3, 3, 3, 3), (4, 4, 4, 3), 
(5, 5, 5, 1), (6, 6, 6, 1);

Insert into orders values (1, 1, '2025-06-16', 7248, 'Address 1'), 
(2, 2, '2025-06-15', 3136, 'Address 2'), 
(3, 3, '2025-06-14', 4679, 'Address 3'), 
(4, 4, '2025-06-13', 4993, 'Address 4'), 
(5, 5, '2025-06-12', 7791, 'Address 5'), 
(6, 6, '2025-06-11', 3807, 'Address 1');

Insert into order_items values (1, 1, 1, 1), (2, 2, 2, 2), (3, 3, 3, 2), 
(4, 4, 4, 3), (5, 5, 5, 2), (6, 6, 6, 3);

--TO DISPLAY TABLE VALUES
select * from customers
select * from products
select * from cart
select * from orders
select * from order_items

-------------------------------------------------------------------------------
--1) To list names and email IDs of customers who placed orders above ₹5000 (Sub query, where)
select * from customers
select * from orders

Select name, email 
from customers 
where customer_id IN (Select customer_id 
                      From orders 
                      Where total_price > 5000);

--2) To show each product's name and total quantity ordered of each products (group by, aggregate(sum))
select * from products
select * from order_items

Select p.name, Sum(oi.quantity) as total_ordered
From products p
Inner Join order_items oi
ON p.product_id = oi.product_id
Group by p.name;

--3) To retrieve all customer names and their order's total price (INNER JOIN, ORDER BY, DESC)
select * from customers
select * from orders

Select c.name, o.total_price
From customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id
Order by o.total_price desc;

--4) To find customers who haven’t placed any orders (LEFT JOIN, WHERE)
Select * from customers
select * from orders

Insert into customers values (7, 'Stu', 'stu@gmail.com', 'pass7');

Select c.*
From customers c 
LEFT JOIN orders o 
ON c.customer_id = o.customer_id 
Where o.order_id IS NULL;

--5) To list all products that were not added to any cart (RIGHT JOIN, WHERE)
Select * from products
Select * from cart

Insert into products values (7, 'Smartwatch', 1999, 'Wearable tech', 15);

Select p.name as Products_Not_InCart
From cart c
RIGHT JOIN products p 
ON c.product_id = p.product_id
Where c.product_id IS NULL;

--6) To display order ID and total number of products in each order (GROUP BY, Aggreagate(SUM))
Select * from order_items

Select order_id, Sum(quantity) as total_products
From order_items
Group by order_id;

--7) To show the product(s) with the maximum stock available (Aggregate(max), SUBQUERY)
Select * from products

Select * from products 
Where stockQuantity = (Select MAX (stockQuantity) from products);

--8) Get all customers who have placed at least one order (EXISTS, SUB QUERY)
Select * from customers
Select * from orders

Select name 
From customers c
Where EXISTS 
    (Select 1 
     From orders o 
     Where o.customer_id = c.customer_id);

--9) To find total spending per customer (GROUP BY, Aggregate(SUM))
Select * from customers
Select * from orders

Select c.name, Sum(o.total_price) as total_spent
From customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id
Group by c.name;

--10) To list top 3 most expensive products (TOP function, desc)
Select * from products

Select TOP 3 name, price
From products
Order by price Desc;

--11) List all orders placed between 2025-06-12 and 2025-06-15
Select * from orders

Select order_id, customer_id, order_date, total_price
From orders
Where order_date BETWEEN '2025-06-12' AND '2025-06-15';

--12) To get product names and their prices where price is above average (SUB QUERY, Aggregate(Avg))
Select * from products

Select name as product_name, price 
From products 
Where price > (Select avg(price) From products);

--13) To find total quantity of each product in the cart (GROUP BY, Aggreagate(SUM))
Select * from cart
Select * from products

Select p.name as product_name, Sum (ct.quantity) as Total_quantity
From cart ct
INNER JOIN products p
ON ct.product_id = p.product_id
Group by p.name;

--14) To list customers who share the same password (SELF JOIN)
Select * from customers

SElect c1.name as Customer1, c2.name as Customer2
From customers c1
JOIN customers c2 --self join
ON c1.password = c2.password AND c1.customer_id <> c2.customer_id;

--15) To show the earliest and latest order date (MIN, MAX)
Select * from orders

Select Min (order_date) as earliest, 
       Max (order_date) as latest 
From orders;

--16) To retrieve customer and product names for all ordered items (INNER JOIN)
SElect * from order_items
Select * from orders
Select * from customers
Select * from products

Select c.name as customer_name, p.name as product_name
From order_items oi
INNER JOIN orders o
ON oi.order_id = o.order_id
INNER JOIN customers c
ON o.customer_id = c.customer_id
INNER JOIN products p
ON oi.product_id = p.product_id;

--17) To list all customer names and all product names (UNION) --SET
Select * from customers
Select * from products

Select name From customers
UNION
Select name From products;

--18) To list customer names that are also product names (INTERSECT) --SET
Select * from customers

Select name From customers where name IN (Select name From products);

Select name From customers
INTERSECT
Select name From products;

--19) To list customers who have not added anything to the cart (EXCEPT, NOT IN) --SET
Select * from customers

Select name From customers 
EXCEPT 
Select name From customers c
INNER JOIN cart ct
ON c.customer_id = ct.customer_id;

--20) To list customers who placed more than one order (Aggregate, GROUP BY, HAVING)
Select * from customers
Select * from orders

Select c.name, count(o.order_id) as order_count
From customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id
Group by c.name
having count(o.order_id) > 1;

--21) Find number of days since each order was placed (DateDiff)
Select * from orders;

Select order_id, order_date, 
DATEDIFF(DAY, order_date, GETDATE()) as days_since_order
From orders;

--22) Cross Join
Select * from customers
CROSS JOIN
products

--23) To display order dates greater than 20 days --Task
Select * from orders

Insert into orders values (7, 1, '2024-12-01', 2500, 'Address 7');

Select order_id, order_date from orders
Where DATEDIFF(DAY, order_date, GETDATE()) > 20;