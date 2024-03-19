SELECT TOP 1 m.mechanicName,SUM(sm.hours) sumHours
FROM Mechanic m 
INNER JOIN ServiceMehanic sm ON m.mechanicID = sm.mechanicID
INNER JOIN ServiceTicket st ON st.serviceTicketID = sm.serviceTicketID
WHERE YEAR(st.dateReceived) = 2021 
	AND YEAR(st.dateReturned) = 2021
GROUP BY m.mechanicID,m.mechanicName
ORDER BY SUM(sm.hours) DESC