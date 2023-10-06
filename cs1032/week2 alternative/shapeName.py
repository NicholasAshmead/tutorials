while True:
    try:
        sides = int(input("Enter the number of sides the shape has\n> "))
        if sides > 10 or sides < 3:
            print("You must enter a number between 3 and 10 inclusive.")
        else:
            break
    except:
        print("You need to enter an integer")

shapeNames = [
"circle",
"semicircle",
"triangle",
"square",
"pentagon",
"hexagon",
"heptagon",
"octogon",
"nonagon",
"decagon"
]

print(f"The name of the shape is {shapeNames[sides-1]}")