# Fill in the exercises below per instructions
# If you see  "Process finished with exit code 0"
# in console please run the right file

# 1 point:
# create the function named "exampleOne" that will return "I am alive! Alive!".
# do it before you run the test file
def exampleOne():
    print("I am alive! Alive!")

# 1 point:
# create the function named exampleTwo, that will have one input parameter.
# take this parameter and add it to "And this alive too: " after that then return
def exampleTwo(paramOne):
    return 'And this is alive too: ' + paramOne
animal = "Dog"
print(exampleTwo(animal))

# 1 point:
# create the function named  exampleThree, that will have three input parameters.
# return the single string with element separated with ...
# like so go...utes...example
def exampleThree(paramOne, paramTwo, paramThree):
    return paramOne + "..." + paramTwo + "..." + paramThree
paramOne = "Let's"
paramTwo = "Go"
paramThree = "Utah!"
print(exampleThree(paramOne, paramTwo, paramThree))

# 1 point:
# create the function named exampleFour, that will have two input parameters.
# first one is a text you need to adjust, and second is the leading and trailing
# text that needs to be removed
# Example:
# first param: %%%%HOHOHO%%%%, second %, result HOHOHO
def exampleFour(paramOne, paramTwo):
    return paramOne + paramTwo
paramOne = "%%%%HOHOHO%%%%"
paramTwo = "%"
print( paramOne.strip("%") )


# 3 points:
# create the function named exampleFive, that will have one input parameter.
# change it so all of the question marks are gone
# example: ????Why am i doing this???? => Why am i doing this
def exampleFive(paramOne):
    return paramOne
paramOne = "????Why am I doing this????"
print( paramOne.strip('?') )

# 3 points:
# create the function named exampleSix, that will have one input parameter.
# Take that input parameter and replace all of the "ss" with "s", and "tt" with "t"
def exampleSix(paramOne):
    return paramOne
paramOne = "sssssstttttt"
print(paramOne.replace("ss", "s").replace("tt", "t"))