while True:
    try:
        day = int(input("enter a day of a month as a number"))
        if day > 0 and day <= 31: break
        else: print("That is not a possible day")
    except:
        print("That is not a valid number")

monthNames = [
"january",
"february",
"march",
"april",
"may",
"june",
"july",
"august",
"september",
"october",
"november",
"december"
]

while True:
    month = input("Enter a month (full name in english)").lower()
    if month in monthNames: break
    else: print(f"That is not a real month, or it is incorrectly spelled")

if day == 1 and month == "january": print("New Year's Day")
elif day == 10 and month == "april": print("Good Friday")
elif day == 13 and month == "april": print("Easter Monday")
elif day == 8 and month == "may": print("Early May Bank Holiday")
elif day == 25 and month == "may": print("Spring Bank Holiday")
elif day == 25 and month == "december": print("Christmas Day")
elif day == 28 and month == "december": print("Boxing Day")