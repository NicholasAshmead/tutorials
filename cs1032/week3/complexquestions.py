# f(x) = x*x, therefore if x = 2, f(x) = 4

def checkFermat(a,b,c,n): # returns true if fermat's conjecture holds
    left = (a**n)+(b**n)
    right = c**n
    return False if right == left else True

print(checkFermat(1,4,5,3))

def magicDate(day,month,year): # year must be 2 digits
    return True if day*month==year else False

print(magicDate(5,2,10))

def medium(a,b,c):
    return (a+b+c)/3

print(medium(int(input("Num 1:")),int(input("Num 2:")),int(input("Num 3:"))))

def euclidesAlgo(x,y):
    if x < y: a=x;x=y;y=a
    r=x%y
    while r!=0:
        x=y;y=r
        r=x%y
    return y

print(euclidesAlgo(6,35))
# 2 prime numbers = 1
# 2 same numbers = returns number
# 2 numbers with common facters: greatest factor
# 2 numbers with no shared factors = 1

def triangleCheck(a,b,c):
    h = max(a,b,c)
    if max==a: t=b+c
    elif max==b: t=a+c
    elif max==c: t=a+b
    if t > h: return True
    else: return False

triangleCheck(3,4,1)