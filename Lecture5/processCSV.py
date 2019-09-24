file = open("tst.csv", "r")
lines = file.readlines()
accountsAsLine = []

for line in lines:
    line = line.strip()
    accounts = line.split(";")
    for account in accounts:
        accountsAsLine.append(account+"\n")
        
file.close()


fileTwo = open("magic.csv", "w")
fileTwo.writelines(accountsAsLine)
fileTwo.close()
