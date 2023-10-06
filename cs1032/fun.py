import random as r
from time import sleep

code = [
'    number1 = input("Enter a number> ")',
'        number1 = float(number1)',
'        print("You need to enter an integer or float")',
'    number2 = input("Enter another number> ")',
'        number2 = float(number2)',
'        print("You need to enter an integer or float")',
'while True:',
'    number3 = input("Enter a third number> ")',
'        number3 = float(number3)',
'        print("You need to enter an integer or float")',
'def greatestOfThree(num1, num2, num3):',
'    if num1 > num2:',
'        if num1 > num3: return num1',
'        else: return num3',
'        if num2 > num3: return num2',
'        else: return num',
]

while True:
    print(r.choice(code))
    sleep(r.randint(0,40)/100)

