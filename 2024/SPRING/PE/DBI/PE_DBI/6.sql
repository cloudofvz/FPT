--Discount of 20% that mean new price = 80% = 0.8 old price
UPDATE product
SET price = price * 0.8
WHERE code_product IN (
SELECT TOP 2 
	p.code_product

FROM invoices i

INNER JOIN inv_detail id 
	ON i.num_invoice = id.num_invoice
INNER JOIN product p 
	ON id.code_product = p.code_product

WHERE YEAR(i.purch_date) = 2023
GROUP BY p.code_product
ORDER BY SUM(id.num_invoice) )