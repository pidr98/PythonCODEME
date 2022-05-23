#1. Napisać funkcję, która oblicza pole koła na podstawie zadanego promienia.

def pole_kola(r):
    pi = 3.14
    radius = pi * r**2
    return radius

radius = float(input('Podaj promien kola: '))
pole = pole_kola(radius)
print('Pole to ', pole)