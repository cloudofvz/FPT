SELECT TOP 5 id_customer as N'Mã khách hàng',
	CONCAT(first_name,' ',last_name) as N'Họ và tên', 
	Email as N'email', 
	phone as N'Số điện thoại'
FROM customer