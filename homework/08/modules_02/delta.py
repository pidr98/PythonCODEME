import math

def inputs():
    a = float(input("Enter A: "))
    b = float(input("Enter B:  "))
    c = float(input("Enter C: "))
    return a, b, c

def delta_calc():
    a, b, c = inputs()
    d1 = math.pow(b, 2)
    d2 = 4 * a * c
    delta = d1 - d2
    x1 = (-b - delta ** 0.5) / (2 * a)
    x2 = (-b + delta ** 0.5) / (2 * a)
    return x1, x2, delta
