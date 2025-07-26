-- create database
CREATE SCHEMA assessment;

USE assessment;

-- create table customer
CREATE TABLE customer (
customer_id INT PRIMARY KEY,
customer_name VARCHAR(45) NOT NULL,
city VARCHAR(45) NOT NULL,
grade INT,
salesman_id INT NOT NULL,
FOREIGN KEY (salesman_id) REFERENCES salesman(salesman_id)
);

-- insert value in table customer
INSERT INTO customer VALUES 
(3002, 'Nick Rimando', 'New York', 100, 5001),
(3007, 'Brad Davis', 'New York', 200, 5001),
(3005, 'Graham Zusi', 'California', 200, 5002),
(3008, 'Julian Green', 'London', 300, 5002),
(3004, 'Fabian Johnson', 'Paris', 300, 5006),
(3009, 'Geoff Cameron', 'Berlin', 100, 5003),
(3003, 'Jozy Altidor', 'Moscow', 200, 5007),
(3001, 'Brad Guzan', 'London', NULL, 5005);

-- create table salesman
CREATE TABLE salesman (
salesman_id INT UNIQUE NOT NULL,
name VARCHAR(45) NOT NULL,
city VARCHAR(45) NOT NULL,
commission FLOAT NOT NULL
);

-- insert value in table salesman
INSERT INTO salesman VALUES
(5001, 'James Hoong', 'New York', 0.15),
(5002, 'Nail Knite', 'Paris', 0.13),
(5005, 'Pit Alex', 'London', 0.11),
(5006, 'Mc Lyon', 'Paris', 0.14),
(5007, 'Paul Adam', 'Rome', 0.13),
(5003, 'Lauson Hen', 'San Jose', 0.12);

-- show table values
SELECT * FROM customer;
SELECT * FROM salesman;

-- select customer and salesman using inner join
SELECT customer.customer_name, customer.city, salesman.name, salesman.commission
FROM customer
INNER JOIN salesman
ON customer.salesman_id  = salesman.salesman_id ;