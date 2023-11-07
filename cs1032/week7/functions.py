def thisIsAFunction(a):
    print("This is a function")
    print("It takes a parameter, which is" + a)
    print("It also returns that parameter")
    return a

def anotherFunction(b,c):
    print("This is another function")
    print("it takes two parameters, which it converts into strings, and then concatenates")
    print("It then returns the concatenated string")
    return str(b) + str(c)

def yetAnotherFunction(d,e):
    print("This is yet another function")
    print("It takes two parameters, which it adds together, if they are numbers")
    print("It then returns the result")
    try:
        return d + e
    except:
        print("One or both of the parameters was not a number :(")
        return False
    

print("This program calls the functions in order, more than once, to demonstrate how they work")

print("Calling thisIsAFunction(\"a\")")
print(thisIsAFunction("a"))
print("\n")
print("Calling thisIsAFunction(\"b\")")
print(thisIsAFunction("b"))
print("\n\n\n")

print("Calling anotherFunction(\"c\",\"d\")")
print(anotherFunction("c","d"))
print("\n")
print("Calling anotherFunction(\"e\",\"f\")")
print(anotherFunction("e","f"))
print("\n\n\n")

print("Calling yetAnotherFunction(1,2)")
print(yetAnotherFunction(1,2))
print("\n")
print("Calling yetAnotherFunction(\"g\",\"h\")")
print(yetAnotherFunction("g","h"))
print("\n\n\n")