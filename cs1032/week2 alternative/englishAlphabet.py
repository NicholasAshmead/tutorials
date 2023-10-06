vowels = ["a", "e", "o", "i", "u", "æ", "œ"]

while True:
    try:
        char = input("Enter a letter\n> ")
        break
    except:
        print("You need to enter a single letter")

if char in vowels:
    print(f"The letter {char} is a vowel")
elif char == "y":
    print(f"The letter {char} is a vowel sometimes")
else:
    print(f"The letter {char} is a a constanant")