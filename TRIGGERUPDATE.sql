Create TRIGGER updateDate
ON SP500
AFTER INSERT  AS
BEGIN
UPDATE SP500
SET Date_int = convert(int,convert(varchar(8),TradeDate,112))
END;