# 3.Utwórz zmienną przechowującą dowolny ciąg znaków.
# Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a.
# Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.

x = 'bbbbaaabb'

if len(x) > 5 and 'a' in x:
    print(x.replace('a','z'))
else:
    print('Zbyt mało liter lub brak litery a')