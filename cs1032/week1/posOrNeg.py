while True:
    number1 = input("Enter a number\n> ")
    try:
        number1 = float(number1)
        break
    except:
        print("You need to enter an integer or float")

if number1 == 0:
    print("The number is zero, and therefore is neither positive or negative")
elif number1 == abs(number1):
    print("The number is positive.")
else:
    print("The number is negative.")

