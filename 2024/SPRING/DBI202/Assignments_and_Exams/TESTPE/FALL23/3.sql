SELECT c.custName,c.phone,c.sex,c.cusAddress,COUNT(si.invoiceID) as 'NumberOfInvoiceID'
FROM Customer c
INNER JOIN SalesInvoice si ON si.custID = c.custID
GROUP BY c.custName,c.phone,c.sex,c.cusAddress
HAVING COUNT(si.invoiceID) >= 3
ORDER BY c.custName