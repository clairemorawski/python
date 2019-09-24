#Fill in the exercises below per instructions
#If you see  "Process finished with exit code 0"
# in console please run the right file -- _Test


#1 point
#create function named exampleOne, that will have 2 input parameters.
#return True if they are not equal to each other
def exampleOne(paramOne, paramTwo):
    return paramOne != paramTwo
print(exampleOne(4, 5))
print(exampleOne(5, 5))

#1 point
#create function named  exampleTwo, that will have 3 input parameters.
#return True if all of them are equal to each other
def exampleTwo(paramOne, paramTwo, paramThree):
    if (paramOne == paramTwo and paramTwo == paramThree):
        return True
    else:
        return False
print(exampleTwo(1, 1, 1))
print(exampleTwo(1, 2, 1))

#1 point
#create function named exampleThree, that will have 3 input parameters.
#return True if either first is different from second or second same is the third
def exampleThree(paramOne, paramTwo, paramThree):
    if( paramOne != paramTwo or paramTwo == paramThree):
         return True
    else:
        return False

#2 points
#create function named exampleFour, that will have 2 input parameters.
#if second param is a part of the first one -- return the last letter of first param
#if second param is not a part of the first one -- return first letter of first param
#hint every string -- is an array of letter and can be used as such
def exampleFour(paramOne, paramTwo):
    if paramTwo in paramOne:
        return paramOne[-1]
    else:
        return paramOne[0]
print(exampleFour("utes", "3"))
print(exampleFour("utes", "z"))

#2 points
#create function named exampleFive, that will have 3 input parameters: one array and two singular.
#return "One", if second element is in an array
#return "Two", if third element is in an array
#return "None", if none of the elements are in the array
def exampleFive(paramOne, paramTwo, paramThree):
    if(paramOne.count(paramTwo)):
        return "One"
    elif(paramOne.count(paramThree)):
        return "Two"
    else:
        return "None"
print(exampleFive([1, 2, 3], 1, 2))

#3 points
#create function named exampleSix, that will have 3 input parameters: one array and two singular.
#return "Success" if second element is NOT in the array and number of elements in the array equals to the third element
#return "Not In Success" if second element is NOT in the array and number of elements in the array does not equals to the third element
#return "Length Success"  if second element is in the array and number of elements in the array equals to the third element
#return "Failure" if second element is in the array and number of elements in the array does not equals to the third element
def exampleSix(paramOne,paramTwo,paramThree):
    if(paramOne.count(paramTwo) == 0 and len(paramOne) == paramThree):
        return "Success"
    if(paramOne.count(paramTwo) == 0 and len(paramOne) != paramThree):
        return "Not in Success"
    if(paramOne.count(paramTwo) > 0 and len(paramOne) == paramThree):
        return "Length Success"
    if(paramOne.count(paramTwo) > 0 and len(paramOne) != paramThree):
        return "Failure"
print(exampleSix([1, 2, 3, 4, 5], 2, 5))