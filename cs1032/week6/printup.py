def printDown(text):
    for i in range(len(text)):
        print(text[i])

def printUp(text):
    for i in range(len(text)):
        print(text[-i - 1])

printUp("Good Morning, This Is A Test.")
print("\n\n\n\n")
printDown("Good Morning, This Is A Test.")