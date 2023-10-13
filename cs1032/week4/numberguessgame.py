import random as r
num = r.randint(1,100)
while True:
    while True:
        try: guess = int(input("Guess a number (1 to 100)\n> ")); break
        except: print("Enter a valid number")
    if guess == num: print("Right"); break
    else: print("Wrong")