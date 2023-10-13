def powerofNum(num, terms):
    for i in range(0,terms):
            print(f"{num} raised to the power of {i} is {num**i}")

powerofNum(2,int(input("Enter the number of terms\n> ")))