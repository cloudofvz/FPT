CREATE TRIGGER tr_insert_car
ON Cars
AFTER INSERT
AS
BEGIN
	DECLARE @year INT
	DECLARE @model NVARCHAR(100)
	SELECT @year = year, @model=model FROM inserted
	SELECT *
	FROM Cars
	WHERE year = @year AND model = @model
END;

