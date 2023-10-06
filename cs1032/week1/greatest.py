while True:
    num1 = input("Enter a number\n> ")
    try:
        num1 = float(num1)
        break
    except:
        print("You need to enter an integer or float")

while True:
    num2 = input("Enter another number\n> ")
    try:
        num2 = float(num2)
        break
    except:
        print("You need to enter an integer or float")

if num1 > num2:
    print(f"number1 ({num1}) is greater than number2 ({num2}).")

elif num2 > num1:
    print(f"number2 ({num2}) is greater than number1 ({num1}).")

else:
    print(f"The two numbers ({num1} & {num2}) are equal.")
