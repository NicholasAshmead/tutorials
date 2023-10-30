counts = {'annie' : 42, 'chuck' : 1 , 'jan': 100}

print("\n\n\n\nTASK1")
for key in counts.__reversed__():
    print(key, counts[key])

print("\n\n\n\nTASK2")
for key in counts.__reversed__():
    if key != 'chuck':
        print(key, counts[key])

print("\n\n\n\nTASK3")
lst = list(counts.keys().__reversed__())
print(lst)
for key in lst.__reversed__():
    print(key, counts[key])