guestAges = []; cost = 0
print("Enter guest age, one at a time, once you are done, enter nothing to end. Negative numbers will not be counted")
while True:
    try:
        temp = int(input(">"))
        if temp > 0: guestAges.append(temp)
    except:
        break

for i in range (len(guestAges)):
    if guestAges[i] <= 2: cost += 0
    elif guestAges[i] <= 12: cost += 14
    elif guestAges[i] >= 65: cost += 18
    else: cost += 23

print(f"""
The cost for this group to enter is:
  
  £{cost}.00
""")
