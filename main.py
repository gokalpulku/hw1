import random
random.seed(54236)


class Portfolio(object):
    cash=0
    stocks ={}
    records = ""
    myMutualFunds = {}

    # __init__ is known as the constructor
    def __init__(self):
        pass

    def addCash(self, a):
        self.cash +=a
        self.records += "\n" + "$" + str(a) + " has been added to your account."

    def withdrawCash(self, withdrawnCash):

        if self.cash < withdrawnCash:
            print("You do not have sufficient funds. Your balance is: $", self.cash, " enter a value which is in the range of your balance \n")
            a = input()
            self.withdrawCash(float(a))
        else:
            self.cash = self.cash - withdrawnCash
            self.records += "\n" + "$" + str(withdrawnCash) + " has been withdrawn from your account."

    def buyStock(self, shareValue, stock):

        totalPrice = stock.price * shareValue
        if self.cash >= totalPrice:
            self.cash -= totalPrice
            if stock.symbol not in self.stocks.keys():
                self.stocks[stock.symbol] = [shareValue]
            else:
                finalAmount = self.stocks[stock.symbol] + shareValue
                self.stocks[stock.symbol] = finalAmount
            self.records += "\n"+ str(int(shareValue)) + " shares of " + str(stock.symbol)
            self.records += " has been purchased for $" + str(shareValue) + "."
        else:
            print("Not enough funds.")

    def sellStock(self, symbol, shareValue):
        sellPrice = random.uniform(1, 20)

        if (symbol not in self.stocks.keys()) or (self.stocks[symbol][0] == 0):
            print("This is not in your portfolio.")
        else:
            mySharesAmount = self.stocks[symbol][0]
            if shareValue > mySharesAmount:
                print("You can not sell more than your portfolio.")
            else:
                mySharesAmount = mySharesAmount - shareValue
                self.stocks[symbol] = [mySharesAmount]
                self.addCash(sellPrice * shareValue)
                self.records += "\n" + str(int(shareValue)) + " shares of " + str(symbol)
                self.records += " has been sold for $" + str(sellPrice * shareValue) + ". Sell price is $" + str(
                    sellPrice) + " per share."

    def buyMutualFund(self, myShareValue, mutualFunds):

        buyPrice = random.uniform(1,20) * myShareValue
        if self.cash >= buyPrice:
            self.cash -= buyPrice
            if mutualFunds.symbol not in self.myMutualFunds.keys():
                self.myMutualFunds[mutualFunds.symbol] = [float(myShareValue)]
            else:
                myMutualFundsAmount = self.myMutualFunds[mutualFunds.symbol][0]
                self.myMutualFunds[mutualFunds.symbol] = [myMutualFundsAmount + float(myShareValue)]
            self.records += "\n" + str(float(myShareValue)) + " shares of " + str(mutualFunds.symbol)
            self.records += " has been purchased for $" + str(buyPrice) + "."
        else:
            print("Not enough funds")

    def sellMutualFund(self, symbol, myShareValue):

        if (symbol not in self.myMutualFunds.keys()) or (self.myMutualFunds[symbol][0] == 0):
            print("Sorry, you do not have this mutual fund. ")
        else:
            myMutualFundAmount = self.myMutualFunds[symbol][0]
            if myShareValue > myMutualFundAmount:
                print("Can not sell more than the funds you have in your portfolio")
            else:
                myMutualFundAmount = myMutualFundAmount - myShareValue
                sellPrice = random.uniform(1, 20)
                self.addCash(sellPrice * myShareValue)
                self.myMutualFunds[symbol] = [myMutualFundAmount, 1]
            self.records += "\n" + str(float(myShareValue)) + " shares of " + str(symbol)
            self.records += " has been sold for $" + str(sellPrice * myShareValue) + ". Sell price is $" + str(
                sellPrice) + " per share."

    def printPortfolio(self):
        print("CASH:")
        print(self.cash)
        print("STOCKS: ")
        print(self.stocks)
        print("MUTUAL FUNDS: ")
        print(self.myMutualFunds)

    def history(self):
        print(self.records)

class Stock(object):
    price = 0
    symbol = None
    def __init__(self, p, s):
        self.price = p
        self.symbol = s


class MutualFund(object):
    tickerSymbol = None

    def __init__(self, s):
        self.symbol = s


portfolio = Portfolio()
portfolio.addCash(300)
s=Stock(20,"SXP")
portfolio.buyStock(5,s)
mf1 = MutualFund("DOGE")
mf2 = MutualFund("XRP")
portfolio.buyMutualFund(4.4,mf1)
portfolio.buyMutualFund(7,mf2)
portfolio.printPortfolio()
portfolio.sellMutualFund("DOGE",1)
portfolio.sellStock("SXP",4)
portfolio.printPortfolio()
portfolio.withdrawCash(31)
portfolio.printPortfolio()
portfolio.history()
portfolio.withdrawCash(200)

