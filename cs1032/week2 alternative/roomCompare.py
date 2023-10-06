while True:
    try:
        lengthRoom1 = float(input("Enter the length of the first room\n> "))
        break
    except:
        print("You need to enter an integer or a float")

while True:
    try:
        widthRoom1 = float(input("Enter the width of the first room\n> "))
        break
    except:
        print("You need to enter an integer or a float")

while True:
    try:
        lengthRoom2 = float(input("Enter the length of the second room\n> "))
        break
    except:
        print("You need to enter an integer or a float")

while True:
    try:
        widthRoom2 = float(input("Enter the width of the second room\n> "))
        break
    except:
        print("You need to enter an integer or a float")

floorSpaceRoom1 = lengthRoom1 * widthRoom1
floorSpaceRoom2 = lengthRoom2 * widthRoom2

if floorSpaceRoom1 == floorSpaceRoom2:
    print(f"The room's floor space ({floorSpaceRoom1}) is equal")
elif floorSpaceRoom1 > floorSpaceRoom2:
    print(f"Room one's floor space ({floorSpaceRoom1}) is greater than the floor space of room two ({floorSpaceRoom2})")
else:
    print(f"Room two's floor space ({floorSpaceRoom2}) is greater than the floor space of room one ({floorSpaceRoom1})")