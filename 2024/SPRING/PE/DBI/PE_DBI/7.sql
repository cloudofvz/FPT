SELECT
	i.num_invoice,
	id.*
FROM inv_detail id

RIGHT JOIN invoices i ON id.num_invoice = i.num_invoice