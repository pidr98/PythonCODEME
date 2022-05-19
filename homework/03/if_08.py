# 8.Sortowanie.
# Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych.
# Znajdź największą liczbę.
# Wyświetl liczby od największej do najmniejszej.

a = int(input('Podaj pierwszą liczbę: '))
b = int(input('Podaj drugą liczbę: '))
c = int(input('Podaj trzecią liczbę: '))

max_digit = max(a, b, c)
print('Największa liczba: ', max_digit)

if max_digit == a and b > c:
    print(a, b ,c)
elif max_digit == a and b < c:
    print(a,c,b)
elif max_digit == b and a > c:
    print(b, a, c)
elif max_digit == b and a < c:
    print(b, c, a)
elif max_digit == c and a > b:
    print(c, a, b)
elif max_digit == c and a < b:
    print(c, b ,a)
else:
    print('Błąd')