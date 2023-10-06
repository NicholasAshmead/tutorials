def fractionAdder(n1,d1,n2,d2):
    primeNumbers=[2,3,5,7,9,11,13,17,19,23,29,31]
    d3=d1*d2
    n3=(n1*d2)+(n2*d1)
    for i in range(int(d3**0.2)):
        for i in primeNumbers:
            if ((d3/i) == int(d3/i)) and ((n3/i) == int(n3/i)):
                d3 /= i; n3 /= i
    return int(n3), int(d3)

print(fractionAdder(3,6,5,30))