from bs4 import BeautifulSoup
import urllib.request as urllib2
import pyodbc
import datetime

def getRate():
        
    url = "http://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yield"
    content = urllib2.urlopen(url).read()
    soup = BeautifulSoup(content, "lxml")
    
    # Last day
    table = soup.find("table", attrs={'class' : 't-chart'})
    rows= table.find_all('tr')
    lastrow = len(rows)-1
    cells = rows[lastrow].find_all("td")
    date = cells[0].get_text()
    r3 = float(cells[2].get_text())
    r = r3/100
    return r

def getSpot(ticker):
    import colorama
    from colorama import Fore
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=stairway.usu.edu;DATABASE=5350FIN;UID=fin5350;PWD=aggies2018')
    
    cursor = cnxn.cursor()
    while True:
        try:
            cursor.execute('exec SP1 @Ticker = ' ''+ticker+'' '')
            for row in cursor.fetchall():
                y = [x for x in row]
            return y[0]
            break
        except UnboundLocalError:
            try:
                cursor.execute('exec SP2 @Ticker = ' ''+ticker+'' '')
                for row in cursor.fetchall():
                    y = [x for x in row]
                return y[0]
                break
            except UnboundLocalError:
                try:
                    cursor.execute('exec SP3 @Ticker = ' ''+ticker+'' '')
                    for row in cursor.fetchall():
                        y = [x for x in row]
                    return y[0]
                    break
                except UnboundLocalError:
                    try:
                        cursor.execute('exec SP4 @Ticker = ' ''+ticker+'' '')
                        for row in cursor.fetchall():
                            y = [x for x in row]
                        return y[0]
                        break
                    except UnboundLocalError:
                        try:
                            cursor.execute('exec SP5 @Ticker = ' ''+ticker+'' '')
                            for row in cursor.fetchall():
                                y = [x for x in row]
                            return y[0]
                            break
                        except UnboundLocalError:
                            print(Fore.RED + ' Oops! The results cannot be returned \n The Ticker declared is invalid \n Try Ticker in all Caps surrounded by quotes\'\' for example: \'AAPL\'' )
                            break
                            
def getVol(ticker):
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=stairway.usu.edu;DATABASE=5350FIN;UID=fin5350;PWD=aggies2018')
    cursor = cnxn.cursor()
    while True:
        try:
            cursor.execute('exec SP1 @Ticker = ' ''+ticker+'' '')
            for row in cursor.fetchall():
                y = [x for x in row]
            return y[1]
            break
        except UnboundLocalError:
            try:
                cursor.execute('exec SP2 @Ticker = ' ''+ticker+'' '')
                for row in cursor.fetchall():
                    y = [x for x in row]
                return y[1]
                break
            except UnboundLocalError:
                try:
                    cursor.execute('exec SP3 @Ticker = ' ''+ticker+'' '')
                    for row in cursor.fetchall():
                        y = [x for x in row]
                    return y[1]
                    break
                except UnboundLocalError:
                    try:
                        cursor.execute('exec SP4 @Ticker = ' ''+ticker+'' '')
                        for row in cursor.fetchall():
                            y = [x for x in row]
                        return y[1]
                        break
                    except UnboundLocalError:
                        try:
                            cursor.execute('exec SP5 @Ticker = ' ''+ticker+'' '')
                            for row in cursor.fetchall():
                                y = [x for x in row]
                            return y[1]
                            break
                        except UnboundLocalError:
                            print("")
                            break
                            
def getVolHistoric(ticker,date):
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=stairway.usu.edu;DATABASE=5350FIN;UID=fin5350;PWD=aggies2018')
    cursor = cnxn.cursor()
    while True:
        try:
            sql = 'exec SPdt @Ticker = ?, @Date  =  ?'
            cursor.execute(sql, (ticker,date))
    
            for row in cursor.fetchall():
                y = [x for x in row]
            return y[1]
            break
        except UnboundLocalError:
            print('')
            break
            
            
def getSpotHistoric(ticker,date):
    import colorama
    from colorama import Fore
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=stairway.usu.edu;DATABASE=5350FIN;UID=fin5350;PWD=aggies2018')
    cursor = cnxn.cursor()
    while True:
        try:
            sql = 'exec SPdt @Ticker = ?, @Date  =  ?'
            cursor.execute(sql, (ticker,date))
    
            for row in cursor.fetchall():
                y = [x for x in row]
            return y[0]
            break
        except UnboundLocalError:
            print(Fore.RED + ' Oops! The results cannot be returned \n The Ticker or Date declared is invalid \n Try Ticker in all Caps surrounded by quotes\'\' for example: \'AAPL\' \n Make sure the date is in integer format yyyymmdd')
            break
            
def getDiv():
    div = 0 
    return div
            
class MarketData(object):
    """A class to encapsulate market data variables.
       Especially to be passed to pricing engines.
    """

    def __init__(self, rate = 0, spot = 0, volatility = 0, dividend = 0):
        self.__rate = rate
        self.__spot = spot
        self.__volatility = volatility
        self.__dividend = dividend
        

    @property
    def rate(self):
        return self.__rate

    @rate.setter
    def rate(self, new_rate):
        self.__rate = new_rate

    @property
    def spot(self):
        return self.__spot

    @spot.setter
    def spot(self, new_spot):
        self.__spot = new_spot

    @property
    def volatility(self):
        return self.__volatility

    @volatility.setter
    def volatility(self, new_volatility):
        self.__volatility = new_volatility

    @property
    def dividend(self):
        return self.__dividend

    @dividend.setter
    def dividend(self, new_yield):
        self.__dividend = new_yield
        
    def get_data(self):
        return (self.__spot, self.__rate, self.__volatility, self.__dividend)
    
    
    def default(self, ticker):
        self.__spot = getSpot(ticker) 
        self.__rate = getRate()
        self.__volatility = getVol(ticker)
        self.__dividend = getDiv()
        return (self.__spot, self.__rate, self.__volatility, self.__dividend)
    
        
    def historic(self, ticker,date):
        self.__spot = getSpotHistoric(ticker, date) 
        self.__rate = getRate()
        self.__volatility = getVolHistoric(ticker, date)
        self.__dividend = getDiv()
        return (self.__spot, self.__rate, self.__volatility, self.__dividend)
    
    
    
