monthLengths = [
31,
[28,29],
31,
30,
31,
30,
31,
31,
30,
31,
30,
31]

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
    if month in monthNames:
        if month != "february":
            print(f"The number of days in {month} is {monthLengths[monthNames.index(month)]}")
        else:
            print(f"The number of days in {month} is either 28 or 29")