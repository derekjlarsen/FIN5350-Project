GO 
CREATE PROCEDURE SP1
(
@Ticker char(6)
)
AS
SELECT cast(SP_CLOSE as float) as spot, cast((log(SP_HIGH) - log(SP_low)) as float) as Vol
FROM SP500
WHERE TickerSymbol = @Ticker
and TradeDate = cast(GETDATE() -1 AS DATE)


GO 
CREATE PROCEDURE SP2
(
@Ticker char(6)
)
AS
SELECT cast(SP_CLOSE as float) as spot, cast((log(SP_HIGH) - log(SP_low)) as float) as Vol
FROM SP500
WHERE TickerSymbol = @Ticker
and TradeDate = cast(GETDATE() -2 AS DATE)

GO 
CREATE PROCEDURE SP3
(
@Ticker char(6)
)
AS
SELECT cast(SP_CLOSE as float) as spot, cast((log(SP_HIGH) - log(SP_low)) as float) as Vol
FROM SP500
WHERE TickerSymbol = @Ticker
and TradeDate = cast(GETDATE() -3 AS DATE)

GO 
CREATE PROCEDURE SP4
(
@Ticker char(6)
)
AS
SELECT cast(SP_CLOSE as float) as spot, cast((log(SP_HIGH) - log(SP_low)) as float) as Vol
FROM SP500
WHERE TickerSymbol = @Ticker
and TradeDate = cast(GETDATE() -4 AS DATE)

GO 
CREATE PROCEDURE SP5
(
@Ticker char(6)
)
AS
SELECT cast(SP_CLOSE as float) as spot, cast((log(SP_HIGH) - log(SP_low)) as float) as Vol
FROM SP500
WHERE TickerSymbol = @Ticker
and TradeDate = cast(GETDATE() -5 AS DATE)


---------------------------------------------------------------------

GO 
CREATE PROCEDURE SPdt
(
@Ticker char(6),
@Date date
)
AS
SELECT cast(SP_CLOSE as float) as spot, cast((log(SP_HIGH) - log(SP_low)) as float) as Vol
FROM SP500
WHERE TickerSymbol = @Ticker
and TradeDate = @Date