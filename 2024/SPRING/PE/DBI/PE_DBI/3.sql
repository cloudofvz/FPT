SELECT id_emp N'Mã nhân viên', 
	CONCAT(first_name,' ',last_name) N'họ và tên',
	addr N'Địa chỉ'
FROM employee 
WHERE addr LIKE N'%Nguyễn%'
 