Create table product (pid int, pname varchar(50), price int, description varchar(50) constraint pk_pid PRIMARY key (pid))

Create table orders(oid int, pid int, qty int, total_amt int CONSTRAINT fk_pid FOREIGN KEY(pid) REFERENCES product(pid))

select * from product
select * from orders;

Insert into product values(1, 'a', 1000, 'desc a'),(2,'b',5000,'desc b'),(3,'c',15000,'desc c'),(4,'d',20000,'desc d'),(5,'e',25000,'desc e')
Insert into orders values(101,1,2,2000),(102,2,1,5000),(103,3,1,15000),(104,4,1,20000),(105,5,1,25000),(106,2,2,10000)

--1) display information of products where price>10000
select * from product where price>10000

--2) display information of products where pid 5-15
select * from product where pid between 5 and 15

--3) display information of products where price range of 5000 to 20000
select * from product where price between 5000 and 20000

--4) display order total_amt>20000
select * from orders where total_amt>20000

--5) count products based on price group
select price,count(*) from product group by price
----SELECT *, COUNT(*) OVER (PARTITION BY price) AS product_count FROM product;

--6) count ordrs based on total_amt
select total_amt,count(*) from orders group by total_amt

--7) display the orders where the count of total_amt>5
select total_amt,count(*) from orders group by total_amt having count(*)>5 --no repeated orders

--8) display the min order, max order based on total_amt
select min(total_amt) as MIN, max(total_amt) as MAX from orders

--9) dispay the product infor in descending order
select * from product order by pname desc

--10) display the count of  orders bsaed on group of pid
select pid,count(*) as order_count_pid from orders group by pid

select * from orders
----------------------------------------------------------------------


---SUB-QUERY

select * from student where id in (select id from marks where m1>=60)

--with EXISTS
Select * from student where exists (Select id from marks where m1>=60) -- if inner query is true nd have atleast one row, then it prints all the outer query

--with NOT EXISTS
Select * from student where NOT exists (Select id from marks where m1>=95)


---Co-related Sub Query
Select * from employee WHERE 5 in (Select eid from employee where employee.eid=eid)
select * from employee

--ANY Operator--
Select * from marks;
select * from marks where m1<= ANY (select min(m1) from marks group by m1) --subquery o/p 20,50,90

select * from marks where m2<= ALL (select min(m1) from marks group by m1)

--ALL Operator--
select * from marks where m1<= ALL (select min(m1) from marks group by m1) --subquery o/p 20,50,90

select * from marks where m1>=ALL (select min(m1) from marks group by m1)

-------------Diff Btw ANY and ALL
---ANY : Atleast one value match with inner query result  (OR)
---ALL : every value must match inner query  (AND)
------------------------

select * from orders where total_amt>= ANY (select min(price) from product group by price) --subquery o/p 1000,5000,15000,20000,25000

select * from orders where total_amt>= ALL (select min(price) from product group by price) --subquery o/p 1000,5000,15000,20000,25000

select * from product
select * from orders


select * from product where pid IN (Select pid from orders group by pid having count(*)>2)