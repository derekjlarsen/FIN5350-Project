CREATE TRIGGER deleteload 
ON SP500_daily
AFTER INSERT  AS
BEGIN
INSERT INTO SP500 (TradeDate, TickerSymbol, Adj_Close, SP_Close, SP_High, SP_Low, SP_Open, SP_Volume)
SELECT [Date], TickerSymbol, [Adj Close], [Close], High, Low, [Open], Volume
FROM SP500_daily

DELETE SP500_daily
END;

