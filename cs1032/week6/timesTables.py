def timesTable(num=3, length=12):
    timesTable = []
    for i in range(1, length + 1):
        timesTable.append(num * i)
    return timesTable

print(timesTable(num=int(input("Enter a number to get times table for:"))))