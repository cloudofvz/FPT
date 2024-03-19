SELECT
	al.name as 'name airline',
	ap1.name as 'Name departing airport',
	ap2.name as 'Name arriving airport'
FROM airline al
	INNER JOIN flight f ON al.id = f.airline_id
	INNER JOIN airport ap1 ON ap1.id = f.departing_airport
	INNER JOIN airport ap2 ON ap2.id = f.arriving_airport
WHERE al.name = 'Vietnam Airlines'