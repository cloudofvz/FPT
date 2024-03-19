SELECT p.id [passenger id],
	CONCAT(p.first_name,' ',p.last_name) [full name],
	bo.id [booking id],
	ba.weight_in_kg 
FROM passenger p
INNER JOIN booking bo ON p.id = bo.passenger_id
INNER JOIN baggage ba ON ba.booking_id = bo.id
WHERE ba.weight_in_kg = 30