EXEC sp_databases

--Create database Student1
--Create table student(id int primary key, sname varchar(50), address varchar(50))

exec sp_help student

insert into student values(1,'Abinesh','chennai')
insert into student values(2,'Vijay','blr')
insert into student values(3,'yadav','chennai')
insert into student values(4,'shankar','cbe')
insert into student values(5,'Ram','blr')
insert into student values(6,'kumar','blr')
insert into student values(7,'Lokesh','blr')

--drop database student1

select * from student

alter table student add phone_number int

alter table student drop column phone_number

select* from student

--to alter constraints --to find primary key value assigned
select name from sys.key_constraints where type='PK' and object_name(parent_object_id)='student'
alter table student drop constraint PK__student__3213E83FED64A701

alter table student add constraint PK__student__3213E83FED64A701 PRIMARY KEY(id);

update student set address='chennai' where id=5

select * from student

update student set address='hyderbad', sname='shankar' where id=2

delete from student where id=7

delete from student where address='cbe'

truncate table student

select*from student

insert into student values(1,'Abinesh','chennai')
insert into student values(2,'Vijay','blr')
insert into student values(3,'yadav','chennai')
insert into student values(4,'shankar','cbe')
insert into student values(5,'Ram','blr')
insert into student (id,sname,address) values(6,'kumar','blr')
insert into student values(7,'Lokesh','blr')

update student set sname='kumar' where id=7

select*from student

Create table marks(id int primary key,m1 int, m2 int,foreign key(id) references student(id))
insert into marks values(1,90,80)
insert into marks values(2,50,30)
insert into marks values(3,90,50)
insert into marks values(4,20,30)
insert into marks values(6,90,80)
insert into marks values(7,90,80)
insert into marks values(5,50,60)
select *from marks

select *from marks where m1=90
select id from marks where m1=90

select * from marks where m1<=50
select * from marks where m1<50

--logical operators commands
--and command : all inputs are true result true
select * from marks where m1>=50 and m2>=50

--or command : any input is true results will be true
select * from marks where m1>50 or m1<=90

--not command : opposite of input
select * from marks where m1!=90

select * from marks where not m1!=90

select * from marks where not m1=90

--null
select * from marks where m1 is null
select * from student where sname is null

--not null
select * from marks where m1 is not null
select * from student where sname is not null

--in
select * from marks where m1 in(50,20,10,90)
select * from marks where id in(5,1)

--not in
select * from marks where m1 not in(10)

--Between
select * from marks where m1 between 50 and 80

--like
select * from student where sname like 'a%'
select * from student where sname like '%a'
select * from student where sname like '_a%'
select * from student where sname like '__d%'
select * from student where id like '[2-5]%'
select * from student where sname like '[a-v]%' 

--Order by
---Ascending
select * from student order by sname
---DESC
select * from marks order by m1 desc

--limit nd offset
--select * from student limit 3 offset 2 --not working
--use this instead
SELECT * FROM student
ORDER BY id
OFFSET 2 ROWS FETCH NEXT 3 ROWS ONLY;
--to print from bottom
select top 3 * from student order by id desc

--GROUP BY
select count(id) from marks group by id
select * from marks
select count(m2),m2 from marks group by m2

--GROUP BY Clause Having
select count(m1),m1 from marks group by m1 having count(m1)>1
--select sum(m2),m2 from marks group by m2 having 

--AGGREGATE FUNCTIONS
---MIN()
select min(m2) as M2 from marks
select min(m1) as M1, min(m2) as M2 from marks
--MAX()
select max(m2) as max_marks_M2 from marks
--SUM()
select sum(m2) as Total from marks
select  sum(m1)+sum(m2) from marks
select sum(m1)+sum(m2) from marks where id=1
select (m1+m2) from marks where id=1
--COUNT()
select count(m1) from marks
--AVG()
select avg(m1) from marks
--------------------------------------------------

--Create table employee(eid int primary key,ename varchar(50), dept_id int, basic_salary int)

Insert into employee values(1, 'Anish', 101, 5000)
Insert into employee values(2, 'yadav', 102, 6000)
Insert into employee values(3, 'vinoth', 103, 8000)
Insert into employee values(4, 'santhosh', 101, 20000)
Insert into employee values(5, 'rajesh', 101, 9000)

select * from employee

select dept_id, min(basic_salary

--drop table marks

--Create table marks(id int primary key,m1 int, m2 int,foreign key(id) references student(id))
insert into marks values(1,90,80)
insert into marks values(2,50,30)
insert into marks values(3,90,50)
insert into marks values(4,20,30)
insert into marks values(6,90,80)
insert into marks values(7,90,80)

select * from marks

