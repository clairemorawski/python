#1 point
#create function exampleOne with one input parameter
#the input is an array of numbers
#square each number and return it as a new array
import math
def exampleOne(paramOne, result=None):
    if result is None:
        result = []
    result.extend(p*p for p in paramOne)
    return result
print(exampleOne([1, 2, 3]))

#2 points
#create function exampleTwo with one input parameter
#the input is an array of numbers
#return last 2 elements of the array in a new array with 100 added to each element
def exampleTwo(paramOne):
    return [p + 100 for p in paramOne[-2:]]
print(exampleTwo([1, 2, 3, 4, 5]))

#2 points
#create function exampleThree with one input parameter
#the input is an array of random elements
#return even elements i.e. 2nd, 4th, 6th, etc.
def exampleThree(paramOne):
    return paramOne[1::2]
print(exampleThree([1, 2, 3, 4, 5, 6]))

#5 points
#create function exampleFour with two input parameters
#the first input is an array of numbers, second is a single number
#if an element of the array is divisible by the second parameter without remainder
#add it to the temp array
#if element is either 7 or 12 immediately move out of the loop.
#next operation is to transform each element in temp array to the string element
#return transofrmed elements as an array
#hint: the remainder is calculated through %, i.e 7%2 = 1
def exampleFour(paramOne, paramTwo):
    result = []
    for item in paramOne:
        if(item == 7 or item == 12):
            continue
        if(item%paramTwo == 0):
            result.append(item)
    for i in range(len(result)):
        result[i] = str(result[i])
    return result
print(exampleFour([1, 2, 3, 4, 5, 6, 7, 8], 2))

