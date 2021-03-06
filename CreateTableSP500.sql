
--Create Table
--Create constraints 
CREATE TABLE SP500
 (
	TickerId INT NOT NULL  IDENTITY(1001,1)   PRIMARY KEY,
	TradeDate  date,
	TickerSymbol char(6),
	Adj_Close	decimal(23,13),
	SP_Close	decimal(23,13),
	SP_High		decimal(23,13),
	SP_Low		decimal(23,13),
	SP_Open		decimal(23,13),
	SP_Volume	decimal(35,2)
)

ALTER TABLE SP500
ADD CONSTRAINT NodubsSP500	UNIQUE CLUSTERED
(
Tradedate, TickerSymbol
)
