SELECT p.product_name,i.purch_date,i.order_status
FROM invoices i 
INNER JOIN inv_detail id ON id.num_invoice = i.num_invoice
INNER JOIN product p ON id.code_product = p.code_product
WHERE i.order_status = N'Chưa thanh toán đủ'
	AND YEAR(i.purch_date) = 2023
	AND MONTH (i.purch_date) = 9