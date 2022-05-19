# 2.Pobierz dwie liczby całkowite od użytkownika i oblicz ich sumę.
# Jeśli suma jest większa niż 100, wyświetl wynik, w przeciwnym wypadku wyświetl “Koniec”.

l1 = float(input('podaj pierwszą liczbę: '))
l2 = float(input('podaj drugą liczbę: '))

suma = l1 + l2
if (suma) > 100:
    print(suma)
else:
    print('Koniec')