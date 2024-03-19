CREATE PROC proc_serviceTicket_part 
@serviceTicketID INT, @numberofparts INT OUTPUT
AS
BEGIN
	SELECT @numberofparts=COUNT(partID) FROM PartsUsed
	WHERE serviceTicketID = @serviceTicketID
	GROUP BY serviceTicketID
END;

DECLARE @x INT
EXEC proc_serviceTicket_part 10111236 ,@x OUTPUT
SELECT @x