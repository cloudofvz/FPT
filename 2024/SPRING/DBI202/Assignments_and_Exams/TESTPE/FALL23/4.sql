SELECT cu.custName,ca.model,st.serviceTicketID,st.dateReturned
FROM Customer cu
INNER JOIN ServiceTicket st ON cu.custID = st.custID
INNER JOIN Cars ca ON st.carID = ca.carID
WHERE YEAR(st.dateReturned)=2021 AND MONTH(st.dateReturned) <=3
ORDER BY st.serviceTicketID DESC