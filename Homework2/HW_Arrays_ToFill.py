#Fill in the exercises below per instructions
#If you see  "Process finished with exit code 0"
# in console please run the right file -- _Test

#1 point:
#create the function named  "exampleOne",that will have one input parameter.
#Function should return double length of the array
def exampleOne(paramOne):
   return 2*len(paramOne)
print(exampleOne([0,1,3,4,5]))

#1 point:
#create the function named exampleTwo, that will have one input parameter.
#return second to last element from array
def exampleTwo(paramTwo):
    return paramTwo[-2]
print(exampleTwo([1,2,3,4,5]))

#1 point:
#create the function named  exampleThree, that will have three input parameters.
#return an array consisting of those 3 elements using no more than 2 lines
def exampleThree(x, y, z):
    return [x, y, z]

#1 points:
#create the function named  exampleFour, that will have one input array parameter .
#return an array created from first, fourth and sixth element of the input array using no more 2 lines
def exampleFour(testArray):
    return [testArray[0], testArray[3], testArray[5]]
print(exampleFour([0, 1, 2, 3, 4, 5, 6, 7]))

#2 points:
#create the function named exampleFive,  that will have one input array parameter and one singular
#return an input array with second parameter added to it
def exampleFive(input_array, arg1):  # where x is an array and y is an single input
    input_array.append(arg1)
    return input_array
exampleFive([3], 4)  # will become [3,4]

#2 points
#create the function named exampleSix,that will have three input parameters array, number, string
#remove an element from input array under the index indicated by second input parameter
#replace second element in the input array with string from third parameter
def exampleSix(arrayTwo, number, string):
    del arrayTwo[number]
    arrayTwo[1] = string
    return arrayTwo
#2 points
#create the function named exampleSeven, that will have one input array parameter and one singular
#remove first two elements from an array and add the second parameter to the end of an array
#please use no more than 3 lines
def exampleSeven(arrayThree, x):
    del arrayThree[0:2]
    arrayThree.append(x)
    return arrayThree

print(exampleSeven([0, 1, 2,3, 4], 5))