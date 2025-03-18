import random


class Stock(object):
    ticker = ""

    def __init__(self, ticker):
        self.ticker = ticker

    def __str__(self):
        return f"Stock: {self.ticker} with price {self.get_price}"

    def get_price(self, _date):
        # _date unused because the price is random for example porpuses
        # Historical prices can be obtained with diferent services/libraries 
        # https://www.linkedin.com/posts/jos%C3%A9-alejandro-betancourt-montellano-4477065b_fintech-stocks-python-activity-7306064418457464833-TAIy?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAy9rvcBIHJim4Zftl6-Yvhj5U2mNek4Ozs
        return random.random() * 100


class Portfolio(object):
    stocks = []
    
    def __init__(self, stocks):
        self.stocks = stocks

    def get_profit(self, start_date, end_date):
        start_amount = sum(stock.get_price(start_date) for stock in self.stocks)
        final_amount = sum(stock.get_price(end_date) for stock in self.stocks)
        return round((final_amount - start_amount) / start_amount * 100, 2)


google = Stock("GOOG")
apple = Stock("AAPL")
amazon = Stock("AMZN")
portfolio = Portfolio([google, apple, amazon])
print("My Profit", portfolio.get_profit("2025-01-01", "2025-03-04"), "%")
