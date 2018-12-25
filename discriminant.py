from math import sqrt
a = int(input("Enter a "))
b = int(input("Enter b "))
c = int(input("Enter c "))

d = b**2 - 4 * a * c
if d < 0:
    print("Your equation has no real roots")
elif d >= 0:
    ds = sqrt(d)
    x1 = (-b + ds)/2*a
    x2 = (-b - ds)/2*a
    print(x1, x2)