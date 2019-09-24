csv = open("grades.csv", "w")
header = "Class,Term,Grade\n"
lines = ["FINAN5330,F19,4.0\n",
        "FINAN3030,F19,3.9\n",
        "QUAMO3030,F19,3.7\n",
        "GOLF1010,F19,5.0\n"]
csv.write(header)
csv.writelines(lines)
csv.close()

csvRead = open("grades.csv", "r")
lines = csvRead.readlines()
overallGPA = 0
majorGPA = 0
dictionary = {"Overall":overallGPA, "Major":majorGPA}
for lineNumber in range(1, len(lines) ):
    line = lines[lineNumber]
    line = line.strip()
    columns = line.split(",")
    columnC = columns[2]
    columnA = columns[0]
    dictionary["Overall"] = dictionary["Overall"] + float(columnC)
    if "FINAN" in columnA:
        dictionary["Major"] = dictionary["Major"] + float(columnC)
average = dictionary["Overall"]/(len(lines)-1)
print(dictionary)
csvRead.close()