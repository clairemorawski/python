class Stock:
    # Stock must have ticker (name)
    def __init__(self, iTicker, iExchange, iPrice):
        self.ticker = iTicker
        self.exchange = iExchange
        self.country = "US"
        self.price = iPrice
        self.dividend = 0

    def printYourself(self):
        printTemplate = "I am representing a public equity in {} company, traded at {} exchange, located in {}"
        textToPrint = printTemplate.format(self.ticker, self.exchange, self.country)
        return(textToPrint)

    def setDividend(self, iDividend):
        if iDividend < 0:
            print("Dividend could not be negative")
            return
        self.dividend = iDividend

    def calculateDividendYield(self):
        return self.dividend/self.price