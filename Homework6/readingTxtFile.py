#What you need to do is to transform the file Mkt_data_test.txt
#to the format like in file in the screenshot
#
#Your steps to get there:
#1.Create a header line with following columns: Time;Bid\Ask;Price;Volume. NOTE NO SPACES
#2.Remove all of the timestamp lines, i.e ======== Data: .....
#3.Remove the 1900-01-01 from the timestamp but leave the time itself
#4.Get rid of all spaces and empty lines
#5.Replace 0 or 1 in the second position with Bid or Ask, Bid for 0, Ask for 1
#6.Save the header line and properly formatted lines to the COMMA-SEPARATED csv file named mktDataFormat.csv
#

file = open("Mkt_data_test.txt", "r")
lines = file.readlines()
file.close()

newLines = []

header = "Time,Bid\Ask,Price,Volume"
newLines.append(header+"\n")
# file.write(header)
file.close()

for line in lines:
    if "=" in line: continue
    line = line.replace(' 0 ',"Bid")
    line = line.replace(' 1 ',"Ask")
    line = line.replace(';', ',')
    line = line.replace("Data", '')
    line = line.replace("\n", '')
    line = line.replace('\t\t\t', '')
    line = line.replace('1900-01-01', '')
    line = line.strip()
    if len(line)>1: newLines.append(line+'\n')

finalFile = open("mktDataTest.csv", "w")
finalFile.writelines(newLines)
file.close()



