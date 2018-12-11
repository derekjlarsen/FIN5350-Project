from probo.marketdata import MarketData
from probo.payoff import VanillaPayoff, call_payoff, put_payoff
from probo.engine import BinomialPricingEngine, AmericanBinomialPricer 
from probo.facade import OptionFacade
import numpy as np

## Set up the market data


thedata = MarketData()
#thedata.historic('ZION', 20181011)
result = thedata.default('AAPL')
expiry = 1.0 
strike = result[0] + 10 
thecall = VanillaPayoff(expiry, strike, call_payoff)
theput = VanillaPayoff(expiry, strike, put_payoff)

## Set up the European Binomial pricer
steps = 3 
pricer = AmericanBinomialPricer
binomengine = BinomialPricingEngine(steps, pricer) 

## Calculate the price
option1 = OptionFacade(thecall, binomengine, thedata)
price1 = option1.price()
print("The call price via American Binomial is: {0:.3f}".format(price1))
option2 = OptionFacade(theput, binomengine, thedata)
price2 = option2.price()
print("The put price via American Binomial is: {0:.3f}".format(price2))


