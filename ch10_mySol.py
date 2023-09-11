
from dataclasses import dataclass
from typing import List
from functools import total_ordering

@dataclass(frozen=True)
class Stock():
    ticker: str
    price: float
    dividend: float = 0
    dividend_frequency: int = 4

    @property
    def annual_dividend(self):
        return self.dividend * self.dividend_frequency

@total_ordering
@dataclass()
class Position():
    stock: Stock
    shares: int

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError("The given instance is not of same type")
        else:
            return self.shares*self.stock.price == other.shares*other.stock.price
        
    def __gt__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError("The given instance is not of same type")
        else:
            return self.shares*self.stock.price > other.shares*other.stock.price

@dataclass()
class Portfolio():
    holdings: List[Position]

    @property
    def value(self):
       return sum([pos.stock.price*pos.shares for pos in self.holdings])
    
    @property
    def portfolio_yield(self):
        return round(sum([pos.stock.annual_dividend*pos.shares for pos in self.holdings])/self.value, 6)

if __name__ == '__main__':

    MSFT = Stock(ticker="MSFT", price=360, dividend=0.62, dividend_frequency=4)
    LMT = Stock("LMT", 360, 2.80, 4)
    GOOGL = Stock("GOOGL", 2200, 0, 0)

    LMT # Stock(ticker='LMT', price=360, dividend=2.8, dividend_frequency=4)

    LMT.dividend = 3.2 # FrozenInstanceError: cannot assign to field 'dividend'

    LMT.annual_dividend # 11.2

    p1 = Position(MSFT, 100)
    p2 = Position(LMT, 100)
    p3 = Position(GOOGL, 10)

    p2 # Position(stock=Stock(ticker='LMT', price=360, dividend=2.8, dividend_frequency=4), shares=100)

    p2 == p1 # True

    p2 <= p3 # False

    portfolio = Portfolio(holdings=[p1, p2, p3])
    portfolio.portfolio_yield # 0.014553

    f"{portfolio.portfolio_yield:.2%}" # '1.46%'

    portfolio.value # 94000

    f"${portfolio.value:,.2f}" # '$94,000.00'