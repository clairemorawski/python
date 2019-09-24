def doSimpleCalculations():
# create variable equal to 99999
    mathA = 99999
# create variable equal to 11111
    mathB = 11111
# return first variable divided by the second one
    return(mathA/mathB)
print( doSimpleCalculations() )

def combineStringsSimple():
# create variable University of
    variableA = "University of "
# create variable Utah
    variableB = "Utah "
# create variable Rules
    variableC = "Rules"
# return University of Utah Rules
    return ( variableA + variableB + variableC )
print(combineStringsSimple())

def combineNumsStrings():
# create number variable 32000
    numberA = 32000
# create variable University of Utah has
    nounA = "University of Utah has "
# create variable students
    nounB = " students"
# combine all of the variables so you would get University of Utah has 32000 students
    return ( nounA + str(numberA) + nounB )
print (combineNumsStrings())


# create a function named convertStringToNum, that will have one input parameter
# take that input parameter, convert it to float and divide by 50
# return the result

def convertStringToNum(paramOne):
    converted = float(paramOne)
    return converted/50
print(convertStringToNum(100))