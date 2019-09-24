import Lecture3.objects.stock as stFile

testStock = stFile.Stock("SNAP", "NYSE",16)
# print(testStock.ticker)
# print(testStock.exchange)
# print(testStock.country)
print("Old Dividend:", testStock.printYourself())
testStock.setDividend(3)
print("New Dividend:", testStock.dividend)

testStockTwo = stFile.Stock("GS", "NASDAQ",200)
print(testStockTwo.printYourself())
testStockTwo.setDividend(6)
print("GS yield:", testStockTwo.calculateDividendYield())

testStockThree = stFile.Stock("GAZPROM", "MOEX",240)
testStockThree.country = "RUS"
testStockThree.setDividend(10)
print("GAZPROM yield:", testStockThree.calculateDividendYield())
print(testStockThree.printYourself())