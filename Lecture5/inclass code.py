file = open("first_file.txt", "w")
firstLine = "Something strange in the neighborhood\n"
secondLine = ""
file.write(secondLine)
file.write(thirdLine)
file.writelines(array)
file.close()

# fileTwo = open("first_file.txt", "a")
# # write your name's first text file
# # file created in python
# fileTwo.write("Claire Morawski is learning python\n")
# fileTwo.close()

fileThree = open("first_file.txt", "r")
contents = fileThree.read()
moreThan7Letters = []
for line in lines:
    # to remove everything except text itself:
    line = line.strip()
    if('\\' in line): continue
    if(len(line)>6):
        moreThan7Letters.append(line)
print(moreThan7Letters)
fileThree.close