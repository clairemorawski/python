from Lecture2.lib import codeComplete

def bake(parameter):
    print(parameter + " is baked")

def fry(paramOne):
    print(paramOne + " is fried")

def useRange(paramOne , paramTwo):
    frying = paramOne + " is fried"
    baking = paramTwo + " is baked"
    return frying + " " + baking
result = ( useRange( "Fish" , "Pie" ) )
print( result )

string = "Five "
length = len(string)
# print("The length is ",length)

text = "BYU Rules"
# print(text)
text = text.replace("BYU", "Utah")
print(text)
template = "{} was founded in {}. It has {} students."
populated = template.format("U of U", 1850, 32000)
populatedTwo = template.format("Harvard", 1643, 120000)
print(populated, populatedTwo)






#
# bake("Fish")
# bake("Apple")
# fry("Egg")
# fry("Bacon")


# codeComplete()