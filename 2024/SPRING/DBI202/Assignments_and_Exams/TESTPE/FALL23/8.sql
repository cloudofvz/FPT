CREATE PROC proc_salesPerson_invoice
@salesID DECIMAL, @numberOfInvoices INT OUTPUT
AS
BEGIN
	SELECT @numberOfInvoices = COUNT(invoiceID)
	FROM SalesInvoice
	WHERE salesID = @salesID
	GROUP BY salesID
END;