while True:
    year = input("Enter a year\n> ")
    try:
        year = int(year)
        break
    except:
        print("You need to enter an year as a number")

if year%4 == 0:
    if year%100 == 0 and year%400 != 0:
        print(f"The year {year} is not a leap year.")
    else:
        print(f"The year {year} is a leap year.")
else:
    print(f"The year {year} is not a leap year.")
