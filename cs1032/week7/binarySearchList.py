import random as r

def listPopulator(size):
    list = []
    for i in range(size):
        list.append(r.randint(0, 1000000))
    return list

def listSorter(size):
    list = listPopulator(size)
    list.sort()
    return list

def binarySearch(list, target): # recursively searches for target in list
    midpoint = len(list)//2
    if list[midpoint] == target:
        return True, list.index(target)
    else:
        return binarySearch(list[midpoint+1:], target) if list[midpoint] < target else binarySearch(list[:midpoint], target)
        
def main():
    size = int(input("Enter the size of the list: "))
    if size < 1: size = 1
    target = int(input("Enter the target number: "))
    list = listSorter(size)
    found, index = binarySearch(list, target)
    print(f"Found {target} at index {index} :)") if found else print(f"{target} not found in list :(")

main()