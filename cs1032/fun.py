import random as r
from time import sleep

code = [
'    number1 = float(input("Enter a number> "))',
'        if number1 == int(number1): return int(number1)',
'while numberStatus == True:',
'    number3 = int(input("Enter a third number> ").lower())',
'        print("You need to enter an integer or float")',
'def greatestOfThree(num1, num2, num3):',
'    if num1 > num2:',
'        if num1 > num3: return num1',
'        for i in range (len(num1)):',
'            if num1[i] > num3[i]: return num1',
'        else: return num3.max(num1, num3)',
'        if num2 > num3: return num2',
'        else: return num.round(num3, 2)',
]

while True:
    print(r.choice(code))
    sleep(r.randint(0,40)/100)

