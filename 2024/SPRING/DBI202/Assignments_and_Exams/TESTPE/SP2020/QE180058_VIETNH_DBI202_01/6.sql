SELECT cust_id
FROM ACCOUNT a
GROUP BY a.CUST_ID
HAVING COUNT(a.ACCOUNT_ID) = 1