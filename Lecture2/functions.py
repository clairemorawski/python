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
#
# bake("Fish")
# bake("Apple")
# fry("Egg")
# fry("Bacon")


# codeComplete()