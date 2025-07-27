select * from employee

Create table emp_salary (sid int, eid int, total_salary int)
Insert into emp_salary values(1,1,20000),(2,2,40000),(3,3,20000),(4,4,60000)

select * from emp_salary

---JOINS---
----Inner JOIN----
select * from employee inner join emp_salary ON employee.eid=emp_salary.eid

select employee.eid, employee.ename, employee.basic_salary, emp_salary.total_salary from employee
INNER JOIN
emp_salary
ON employee.eid = emp_salary.eid; --query too long so, we will use alias

--applying alias
select e.eid, e.ename, e.basic_salary, s.total_salary from employee as e
INNER JOIN
emp_salary as s
ON e.eid = s.eid;

----LEFT JOIN----
select * from employee
LEFT JOIN --also called as left outer join
emp_salary
ON employee.eid = emp_salary.eid;

select e.eid,e.ename,e.basic_salary,s.total_salary from employee as e
LEFT OUTER JOIN
emp_salary as s
ON e.eid = s.eid ORDER BY e.ename desc

----RIGHT JOIN----
select * from employee
RIGHT JOIN --also called as right outer join
emp_salary
ON employee.eid = emp_salary.eid;

select employee.eid, employee.ename, employee.basic_salary, emp_salary.total_salary from employee
INNER JOIN
emp_salary
ON employee.eid = emp_salary.eid where emp_salary.total_salary>=40000

-------------------------------

Create table loan(loan_id int, eid int, sid int, loan_amt int)

Insert into loan values(1,1,1,50000), (2,2,2,90000), (3,3,3,60000)

select * from employee
select * from emp_salary
select * from loan

--doing with 3 tables
select e.eid, e.ename, s.total_salary --, l.loan_amt 
From employee as e
LEFT JOIN emp_salary as s
ON e.eid = s.eid
LEFT JOIN loan as l
ON s.eid = l.eid;

----CROSS JOIN----
select * from employee
CROSS JOIN
emp_salary;

----SELF JOIN----
select * from employee e1, employee e2 where e1.eid = e2.eid

--GROUP BY CLAUSE IN JOINS--
select count (e.eid) as total_count, e.dept_id from employee as e 
INNER JOIN
emp_salary as s
ON e.eid = s.eid GROUP BY e.dept_id;

--HAVING CLAUSE in JOINS--
select count (e.eid) as total_count, e.dept_id from employee as e 
INNER JOIN
emp_salary as s
ON e.eid = s.eid GROUP BY e.dept_id HAVING count (e.eid) > 1


------------------SET OPERATIONS-----------------------
Create table salary(sid int, eid int, salary int)
select * from salary
insert into salary values (1,1,60000), (9,9,50000)

--1) UNION

Select * from emp_salary
UNION
Select * from salary;

--2) INTERSECT

select * from emp_salary
INTERSECT
select * from salary;

--3) EXCEPT

select * from emp_salary
EXCEPT
select * from salary

----------------------------------------------------------
----Joins TASKS----

select * from employee
INSERT INTO employee VALUES (6, 'Frank', 104, 5500);

Create table project (pid int CONSTRAINT pk_pro_id primary key, pname VARCHAR(50), technology VARCHAR(50), duration INT)

Create table project_allocation (pid INT CONSTRAINT fk_pro_id FOREIGN KEY (pid) REFERENCES project(pid), eid int CONSTRAINT fk_eid FOREIGN KEY (eid) REFERENCES employee(eid))
alter table project_allocation add  status VARCHAR(20);


-- Employee
--INSERT INTO employee VALUES(1, 'A', 50000), (2, 'B', 45000), (3, 'C', 47000), (4, 'D', 52000), (5, 'E', 48000), (6, 'F', 55000);

-- Project
INSERT INTO project VALUES (101, 'ProjectA', 'Java', 6), (102, 'ProjectB', 'Python', 3), (103, 'ProjectC', 'Java', 4), (104, 'ProjectD', 'C++', 5);

-- Project_Allocation
INSERT INTO project_allocation VALUES (101, 1, 'in-progress'), (101, 2, 'completed'), (102, 1, 'completed'), (102, 3, 'in-progress'), (103, 4, 'completed'), (103, 2, 'in-progress'), (104, 1, 'completed'), (104, 5, 'in-progress'), (104, 6, 'completed');

--1) List the employee whom the project is allocated - ascending order
Select e.eid, e.ename, e.basic_salary
from employee e
INNER JOIN 
project_allocation pa 
ON e.eid = pa.eid
GROUP BY e.eid, e.ename, e.basic_salary
ORDER BY e.ename;

--2) List the employee whom the project is not allocated - descending order
Select e.eid, e.ename, e.basic_salary
from employee e
LEFT JOIN 
project_allocation pa 
ON e.eid = pa.eid
where pa.eid IS NULL
ORDER BY e.ename desc;

--3) List the project details and the employee details along with the status
select p.pid, p.pname, p.technology, p.duration, e.eid, e.ename, e.basic_salary, pa.status
from project p
inner JOIN project_allocation pa 
ON p.pid = pa.pid
inner JOIN employee e 
ON pa.eid = e.eid;

--4)List the employees who are working in similar projects
SELECT e1.eid, e1.ename, p1.technology
FROM employee e1
JOIN project_allocation pa1 ON e1.eid = pa1.eid
JOIN project p1 ON pa1.pid = p1.pid
WHERE EXISTS (
    SELECT pa2.eid
    FROM project_allocation pa2
    JOIN project p2 ON pa2.pid = p2.pid
    WHERE p1.technology = p2.technology
      AND pa1.eid <> pa2.eid
)
GROUP BY e1.eid, e1.ename, p1.technology;

--5)Count of employees working on similar projects
select p.technology, COUNT(pa.eid) AS emp_count
FROM project p
JOIN project_allocation pa ON p.pid = pa.pid
GROUP BY p.technology
HAVING COUNT(pa.eid) > 1;










-------------------------------------------------------------------

-----------STRING FUNCTION--------------
select ASCII(65) --ASCII value of number will be returned
select char(99) --Value of character is returned

select charindex ('x','xerox') as position

select 'cse' + 'IT'

select RTRIM('IT             ')
select LTRIM('             hexaware')

select len ('computer') --as length_string(to print coln name) (optional)

select DATALENGTH ('computer')

----difference
---Compare two strings and display its soundex value
--soundex: 0 to 4
--0    weak
--4    strong
select DIFFERENCE ('cse', 'cse')
select difference ('cse', 'sdfsf')

--------EXTRACT Character in string--------
Select left('computer base', 3) as string
Select right('computer base', 3) as string

select lower ('ABC')
select upper ('abc')

select upper (ename) from employee
select lower (ename) from employee

select replace ('computer', 'p', 'z')

select reverse ('computer')

select substring ('hexaware chennai', 3, 4)

------------------------MATHEMATICAL FUNCTIONS---------------------

---SCIENTIFIC and TRIG FUNCTION---
select abs(-565.2)

select acos (0.25)

select asin (0.25)

select atan (0.33)

select cot (0.30)

---ROUNDING FUNCTION---
Select ceiling (34.34333)

select round (34.5656, 2)

select floor (34.5664)

-----------
select log(10)

select exp(1)

select pi()

select power (4,2)

select sqrt (64)

select square (4)

---RANDOM function---
select RAND(5)
select rand(5) + 10
select rand(5) * 10

select round (rand(), 2)
----------------------------------------------------------------------------

-----------DATE FUNCTIONS--------------
select getdate()

select datepart (Year, '2024-03-12')
select datepart (month, '2024-03-12')
select datepart (Day, '2024-03-12')

SELECT datepart ( Year, getdate())
SELECT datepart ( Month, getdate())
SELECT datepart ( Day, getdate())

select * from student
alter table student add dob datetime

UPDATE student
SET dob = '1990-10-12'
WHERE sname = 'Abinesh';

UPDATE student
SET dob = '1991-05-14'
WHERE sname = 'Vijay';

UPDATE student
SET dob = '2021-10-10'
WHERE sname = 'yadav';

select id, sname, datepart (year, dob) as Birth_Year, datepart ( month, dob) as month from student

select datename ( month, dob) from student
select datename ( DAY, dob) from student
select datename ( YEAR, dob) from student

select current_timestamp as current_time1
select current_timestamp+7 as delivery_date
select current_timestamp-7 as due_Overdate

select * from student where dob < current_timestamp-50

select datediff(day, '2024/01/23', '2024/10/28') as date_diff
select datediff(Month, '2024/01/23', '2024/10/28') as date_diff
select datediff(Year, '2024/01/23', '2024/10/28') as date_diff

select id, sname, dob, datediff (year, dob, current_timestamp) as AGE_Year from student
select id, sname, dob, datediff (Month, dob, current_timestamp) as AGE_Month from student
select id, sname, dob, datediff (Day, dob, current_timestamp) as AGE_Day from student

select isdate ('2024/01/31')





















