SELECT TOP 10 f.id 'flight id' , f.departure_time,f.arrival_time,SUM(ba.weight_in_kg) 'Total weight'
FROM flight f
LEFT JOIN booking bo ON bo.flight_id = f.id
INNER JOIN baggage ba ON bo.id = ba.booking_id
GROUP BY f.id , f.departure_time,f.arrival_time
ORDER BY SUM(ba.weight_in_kg) DESC