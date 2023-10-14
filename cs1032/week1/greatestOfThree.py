while True:
    number1 = input("Enter a number\n> ")
    try:
        number1 = float(number1); break
    except:
        print("You need to enter an integer or float")

while True:
    number2 = input("Enter another number\n> ")
    try:
        number2 = float(number2); break
    except:
        print("You need to enter an integer or float")

while True:
    number3 = input("Enter a third number\n> ")
    try:
        number3 = float(number3); break
    except:
        print("You need to enter an integer or float")

def greatestOfThree(num1, num2, num3):
    if num1 > num2:
        if num1 > num3: return num1
        else: return num3
    else:
        if num2 > num3: return num2
        else: return num3

print(f"The greatest of the 3 numbers is: {greatestOfThree(number1, number2, number3)}")
