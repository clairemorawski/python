turtle = ["One", "Two", "Three"]

print(turtle)

so = "Maybe So"
print(so)

fourthElement = "Whatever"


def autoFunction(fourthElement):
    turtle.append(fourthElement)
    for elem in turtle:
        string = "The current element is: {}".format(elem)
        print(string)
autoFunction("Whatever")