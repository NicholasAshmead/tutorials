def pwr(n, p):
    if p == 0: return 1
    else: return n * pwr(n, p - 1)

n = int(input("Enter a base:"))
p = int(input("Enter a power:"))

print(pwr(n, p))