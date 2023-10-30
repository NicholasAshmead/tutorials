import random as r
num1 = r.randint(0,999)
num2 = r.randint(0,999)
sum = num1 + num2

while True:
    guess = int(input("Guess the number (between 0 & 1998): "))
    if guess == sum: break
    else: print("Try again")