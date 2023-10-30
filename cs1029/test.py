setA = {1,2,5,7,234,94}
setB = {1,2,3,4,6,8,9,10}

print(setA&setB) # intersection or AND
print(setA|setB) # union or OR
print(setA-setB) # difference
print(setA^setB) # XOR
'''
------------------
| A | B | A -> B |
------------------
| T | T |   T    |
| T | F |   F    |
| F | T |   T    |
| F | F |   T    |
------------------
'''

# ~ is the same as - but it is symmetric

print("\n\n\n\n")

print(setA.intersection(setB))
print(setA.union(setB))
print(setA.difference(setB))


print("\n\n\n\n")

a = 10 # 1010
b = 6 # 0110
print(a, bin(a))
print(b, bin(b))
 
# Print bitwise AND operation
print("a & b =", a & b, bin(a&b))
 
# Print bitwise OR operation
print("a | b =", a | b, bin(a|b))
 
# Print bitwise NOT operation
print("~a =", ~a, bin(~a))
 
# print bitwise XOR operation
print("a ^ b =", a ^ b, bin(a^b))