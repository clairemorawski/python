array = [ "Senatus", "Populus", "Que", "Romanus"]

dictionary = { "S": "Senatus", "P": "Populus",
               "Q": "Que", "R": "Romanus", 42: "Meaning of Life in Years" }

dictionary["E"] = "Emperium"
# print( array[0] )
# print ( dictionary[42] )

print(dictionary)

keys = list(dictionary.keys())
values = list(dictionary.values())
print(keys[3])
print(keys)
print(values)

print(dictionary.pop("E"))
print(dictionary)

# empty arrays:
# dictionary = {}
# dictionary = dict()

for elem in array:
    print(array)

for key in dictionary:
    print("Key is: {}, value is {} ". format(key, dictionary[key]) )

for key, value in dictionary.items():
    print("Key is: {}, value is {}". format(key, value) )

englishRussian = {"Sun": 'Solnce', "Water": 'Voda', "Son": 'Syn'}
for key, value in englishRussian.items():
    print("{} is {} in Russian". format(key, value))

print("S" == " S ")
key = " S "
print(dictionary)
if "S" in key:
    dictionary["S"] = englishRussian["S"] + " One more "

print(dictionary, englishRussian)