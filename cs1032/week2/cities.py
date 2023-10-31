s = "Aberdeen, Dundee, Edinburgh, Glasgow"

# by index in string
print(s[:8])
print(s[10:16])
print(s[18:27])
print(s[29:36])

# or with list splitting
cities = s.split(", ")
print(cities[0])
print(cities[1])
print(cities[2])
print(cities[3])

'''
Immutable - unchanging over time or unable to be changed.
'''