while True:
    try:
        triSide1 = float(input("Enter the length of the first side of the triangle\n> "))
        break
    except:
        print("You need to enter an integer or a float")

while True:
    try:
        triSide2 = float(input("Enter the length of the second side of the triangle\n> "))
        break
    except:
        print("You need to enter an integer or a float")

while True:
    try:
        triSide3 = float(input("Enter the length of the third side of the triangle\n> "))
        break
    except:
        print("You need to enter an integer or a float")

if triSide1 == triSide2 == triSide3: # equilateral
    print(f"The triangle is equilateral as all the sides are {triSide1} long.")
elif triSide1 == triSide2 or triSide1 == triSide3 or triSide3 == triSide2:
    print(f"The triangle is isoseles since two sides are the same length.")
else:
    print("The triangle is scalene since the sides are all different lengths.")