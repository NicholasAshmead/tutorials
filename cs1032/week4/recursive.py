def pwr(n, p):
    return 1 if p == 0 else n * pwr(n, p - 1)

n = int(input("Enter a base:"))
p = int(input("Enter a power:"))

print(pwr(n, p))