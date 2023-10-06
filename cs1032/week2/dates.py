date = "11/09/2001"

print(f"Day: {date[:2]}, Month: {date[3:5]}, Year: {date[6:]}")

date = '11/9/2001'
day = date.find('/')
month = date.find('/',day+1)
d = date[0:day]
m = date[day+1:month]
y = date[month+1:]
print ('\nTake apart %s :' % date)
print (f" Day = {d}, Month = {m} , Year = {y}")