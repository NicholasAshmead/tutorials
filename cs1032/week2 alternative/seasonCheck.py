month = input("Enter a month (full name in english)").lower()
day = int(input("Enter a day (number)"))

# winter
if month == "january" or month == "february" or (month == "march" and day < 20) or (month == "december" and day > 20):
    print("Its winter!!!!!!!!")

elif (month == "march" and day >= 20) or month == "april" or month == "may" or (month == "june" and day < 21):
    print("It is spring.")

elif (month == "june" and day >= 21) or month == "july" or month == "august" or (month == "september" and day <22):
    print("Its summer!")

else:
    print("Its autumn")