# 4. Pobierz od użytkownika parzystą listę elementów. Sprawdź czy 2 środkowe elementy są takie same.

digits = input('Podaj parzystą ilość liczb przedzielone spacją: ')
digits = digits.split()
middle_list1 = int((len(digits) / 2) - 1)
middle_list2 = int((len(digits) / 2))


if len(digits) % 2 == 0:
    if digits[middle_list1] == digits[middle_list2]:
        print('srodkowe liczby takie same')
    else:
        print('nie takie same')
else:
    print('Nieparzysta liczba elementow')
