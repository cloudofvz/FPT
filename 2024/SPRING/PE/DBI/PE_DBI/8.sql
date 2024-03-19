CREATE FUNCTION find_customers_by_employee(@id VARCHAR(10))
RETURNS TABLE
AS 
RETURN
(
SELECT 
	CONCAT(c.first_name,' ',c.last_name) as customer_name
FROM employee e 
INNER JOIN invoices i ON e.id_emp = i.id_emp
INNER JOIN customer c ON i.id_customer = c.id_customer
WHERE e.id_emp = @id
)

DECLARE @input_id VARCHAR(10)
SET @input_id = 'NV0001'
SELECT * FROM find_customers_by_employee (@input_id)