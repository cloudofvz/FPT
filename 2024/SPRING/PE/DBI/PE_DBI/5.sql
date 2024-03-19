--Create a temp table to save all customers that buy product in 2023
WITH 
	buyer_in_2023
AS
(SELECT i.id_customer
FROM customer c
INNER JOIN invoices i ON c.id_customer = i.id_customer
WHERE YEAR(i.purch_date) = 2023)

-- Select from customer that have id not in temp
SELECT *
FROM customer
WHERE id_customer NOT IN 
	(SELECT * FROM buyer_in_2023);