-------------CODING CHALLENGE--------------------

--------Loan Management System---------

--DATABASE
Create database LoanDB

--Tables
Create table Customers(customerId INT Identity(1,1) PRIMARY KEY, name VARCHAR(100), emailAddress varchar(100), phoneNumber VARCHAR(20), address varchar(200), creditScore INT);

create table Loans(loanId int Identity(1,1) PRIMARY KEY, customerId int foreign key references Customers(customerId), principalAmount Float, interestRate float, loanTerm int, loanType varchar(50), loanStatus varchar(20))

create table HomeLoan(loanId int primary key foreign key references Loans(loanId), propertyAddress varchar(200), propertyValues INT)

create table CarLoan(loanId int PRIMARY KEY foreign key references Loans(loanId), carModel Varchar(100), carValue int)

--Inserting Values
Insert into Customers values('Giana', 'giana@email.com', '9876543210', 'Califoria', 700),
('James', 'james.doe@email.com', '9123456780', 'NewYork', 750),
('Stefany', 'stefany@email.com', '9012345678', 'Texas', 680);

Insert into Loans values (1, 500000, 7.5, 60, 'HomeLoan', 'Pending'),
(2, 300000, 9.0, 48, 'CarLoan', 'Approved'),
(3, 800000, 8.2, 72, 'HomeLoan', 'Rejected'),
(2, 550000, 8.0, 36, 'CarLoan', 'Pending'),  
(3, 600000, 10.0, 48, 'CarLoan', 'Approved')

Insert into HomeLoan values(1, 'No.12, MG Road, Chennai', 650000),
(3, 'Plot 22, Indiranagar, Bangalore', 900000)

Insert into CarLoan values (2, 'Hyundai Creta', 350000),
(4, 'Maruti Swift', 550000),
(5, 'Tata Nexon', 600000); 

--Displaying tables
select * from Customers
select * from Loans
select * from HomeLoan
select * from CarLoan