SELECT * 
FROM flight f
WHERE MONTH(f.departure_time) = 2 AND YEAR(f.departure_time) = 2023 