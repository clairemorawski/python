text = "Utah Man Am I Ki Yi"

textArray = [ "Utah", "Man", "Am", "I" ]
textCapitalized = []
# printing every single element in the text:
for char in textArray:
    textCapitalized.append( char.capitalize() )
print(textCapitalized)

# print(textArray[0], textArray[2])
# below counts how many elements in an array:
# print(len(textArray))
# below will always reference the last element
# print( text[-5] )
# print(textArray[ len(textArray)-1 ])

# Fan Am printing: from: to: 5-11:
# print( text[5:11] )

textArray[0] = "Utes"
textArray[1] = "We"
textArray[2] = "Are"
variable = textArray.index("I")
# arrayVariable = textArray.append("Utes")
varPartialOne = ["Utes"]
varPartialTwo = ["We", "Are", "!"]
#summation of elements from more than 1 array:
varCompleteOne = varPartialOne + varPartialTwo + ["Yes we are!"]
# print(varPartialOne, varPartialTwo, varCompleteOne)
#print(textArray)
# how to print number of array of a string:
# print(textArray.index("I"))
# print(textArray.index("Utes"))
# ctrl+d
# adding to original function: use append:
# textArray.append("Utes")
# print(textArray)


# removing elements from an array:
# with pop, use index number
# print(textArray.pop(3))
# print(retVariable)

# to use remove: do not use index, but element name itself:
# textArray.remove("Utes")
# print(textArray)

# empty an array:
# emptyArray = []
# emptyArray.append("element1")
# textArray = []
# textArray.clear()
# print(textArray)

# How to match 2 elements from 2 different arrays:
firstNames = ["John", "Jack", "Mary"]
lastNames = ["Smith", "Cook", "Fisher"]
for index in range(0, len(firstNames)):
    print(firstNames[index], lastNames[index])

# How to match 2 elements from 2 different arrays in reverse order:
firstNames = ["John", "Jack", "Mary"]
lastNames = ["Fisher", "Cook", "Smith"]
for index in range(0, len(firstNames)):
    lastNames.reverse()
    print(firstNames[index],lastNames[index])

print(list( range(0,10000,100) ))