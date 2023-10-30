highest = number = int(input("Enter number:"))
while number != 0:
    if number > highest:
        highest = number
    number = int(input("Enter a number:"))

print(highest)