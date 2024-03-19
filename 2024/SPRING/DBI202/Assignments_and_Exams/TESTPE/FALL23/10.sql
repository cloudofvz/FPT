CREATE FUNCTION f_fk (@mechanicID DECIMAL(18,0))
RETURNS TABLE
AS 
RETURN
(
	SELECT m.mechanicID,m.mechanicName,SUM(sm.hours) as sumHours
	FROM ServiceMehanic sm
	INNER JOIN Mechanic m ON sm.mechanicID = m.mechanicID
	WHERE m.mechanicID = @mechanicID
	GROUP BY m.mechanicID,m.mechanicName
)