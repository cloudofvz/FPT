SELECT *
FROM flight
WHERE id IN
(SELECT
    f.id
FROM flight f
    LEFT JOIN booking b ON b.flight_id = f.id
WHERE MONTH(f.departure_time) = 5 and YEAR(f.departure_time)=2023
GROUP BY f.id
HAVING COUNT(b.id) = 0)
;
