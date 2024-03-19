SELECT TOP 1 p.country,COUNT(b.id) as NumberOfPassenger
FROM passenger p 
INNER JOIN booking b ON p.id = b.passenger_id 
GROUP BY p.country
ORDER BY COUNT(b.id) DESC