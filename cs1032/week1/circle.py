pi = 3.1415926535897932384626433832795028841971693993751058209749445923

while True:
    try:
        radius = float(input("Enter circle radius\n> "))
        if radius != 0: break
        else: print("Radius must not be equal to zero")
    except:
        print("You need to enter an integer")

circumference = 2 * pi * radius
area = (radius ** 2) * pi

print(f"""
The circumference of the circle with radius {radius} is {circumference}
The area of this circle is {area}
""")

import math

c = 2 * 4 * math.pi
varName = 30
a = 4 * 3
b = 4 ** 2 
print(a)
print(f"Hello! {a}")