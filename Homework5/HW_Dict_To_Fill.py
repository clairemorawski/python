#1 point
#create a function exampleOne with four input parameters.
#return a new dictionary where 1st and 3rd parameter will be keys,
#and 2nd and 4th will be values, so your key-value pair will be 1st-2nd, 3-4th
def exampleOne(paramOne, paramTwo, paramThree, paramFour):
    return {paramOne: paramTwo, paramThree: paramFour}
print(exampleOne('key1', 'val1', 'key2', 'val2'))

#2 points
#create a function exampleTwo with one parameter which will be an array of arrays, where inner arrays have 2 elements
#iterate over each element in the array and extract first element as a key, second as a value
#construct a dictionary out of them
#e.g input( [ ["key1","value1"], ["key2","value2"] ] -> output dictionary of matching pairs "key1"-"value2", "key2"-"value2"
def exampleTwo(paramOne):
    return {kv[0]: kv[1] for kv in paramOne}
print(exampleTwo([["key1", "value1"], ["key2", "value2"]]))


#2 points
#create a function exampleThree with two input paratmers, first one is a random dictionary, second is a random key
#return the square of retrieved element, if input key(second param) is present in input dictionary(first param)
#if not present, return 0
#create a function exampleThree with two input paratmers, first one is a random dictionary, second is a random key
#return the square of retrieved element, if input key(second param) is present in input dictionary(first param)
#if not present, return 0
def exampleThree(paramOne, paramTwo):
    if paramTwo not in paramOne:
        return 0
    return paramOne[paramTwo] * paramOne[paramTwo]
random_dictionary = {25: 1, 50: 10}
random_key = 50
print(exampleThree(random_dictionary, random_key))

#5 points
#create function exampleFour with two input parameters, first one is an array of letters, second is words
#return the new dictionary where letters are matched with words based on the first letter, i.e. abbreviation
#you can assume that all of the letters and words will be a unique match, i.e. if 5 letters, then there are 5 words
#e.g. inputs ["D","M","V"], ["Motor","Division","Vehicles"] -> out dictionary of "D"-"Division","M"-"Motor","Vehicles"
def exampleFour(paramOne, paramTwo):
    result = {}
    for key in paramOne:
        for value in paramTwo:
            if value.startswith(key):
                result[key] = value
                break
    return result
print(exampleFour(["D","M","V"], ["Motor","Division","Vehicles"]))
