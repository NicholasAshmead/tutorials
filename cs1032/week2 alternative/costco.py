while True:
    try:
        numItems = int(input("Enter the number items\n> ")); break
    except:
        print("You need to enter an integer")

while True:
    try:
        numCost = float(input("Enter the cost to pay\n> ")); break
    except:
        print("You need to enter an integer or float")

if numItems > 30: print(f"Cost to pay: f{numCost*0.5}")
elif numItems > 20: print(f"Cost to pay: f{numCost*0.7}")
elif numItems > 10: print(f"Cost to pay: f{numCost*0.8}")
else: print(f"Cost to pay: f{numCost}")