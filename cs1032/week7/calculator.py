def add(x, y):return x + y
def subtract(x, y):return x - y
def multiply(x, y):return x * y
def divide(x, y):return x / y
def average(x, y):return (x + y) / 2
def power(x, y):return x ** y


print('''
Select an operation:
 1 - Add
 2 - Subtract
 3 - Multiply
 4 - Divide
 5 - Average
 6 - Power
''')

while True:
    choice = input("Select an operation\n> ")
    if choice in ('1', '2', '3', '4', '5', '6'):
        try:
            num1 = float(input("Enter first number\n> "))
            if int(num1) == num1: num1 = int(num1)
            num2 = float(input("Enter second number\n> "))
            if int(num2) == num2: num2 = int(num2)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    elif choice == '5':
        print(f"{num1} and {num2} have an average of {average(num1, num2)}")
    elif choice == '6':
        print(f"{num1} ^ {num2} = {power(num1, num2)}")
    else:
        print("Something went wrong.")
    
    next_calculation = input("Let's do next calculation? (y/n)\n> ").lower()
    if next_calculation == "y": continue
    elif next_calculation == "n": break
    else: print("Invalid Input")

quit()