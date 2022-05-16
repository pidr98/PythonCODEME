# 1.Poproś użytkownika o podanie liczby. Sprawdź czy liczba podana przez użytkownika jest podzielna przez 3 bez reszty i wyświetl komunikat “Twoja liczba jest podzielna przez 3”.
'''
number = int(input('podaj liczbe od 1 do 100: '))
if number % 3 == 0:
    print('twoja liczba jest podzielna przez 3')
else:
    print('nie jest podzielna przez 3')
'''
'''
# 3.
rev1 = int(input('podaj liczbe od 1 do 10: '))
rev2 = int(input('podaj liczbe od 1 do 10: '))
rev3 = int(input('podaj liczbe od 1 do 10: '))

rev123 = (rev1 + rev2 + rev3) / 3

if rev123 > 7:
    print('Bardzo dobra ksiazka')
elif rev123 >= 5:
    print('przecietna')
else:
    print('nie warta uwagi')
'''
'''
# 5.
password = input('Hasło: ')

if len(password) < 8:
    print('Hasło musi zawierać przynajmniej 8 znaków!')

if password.isalnum() and (password.isdigit() or password.isalpha()):
    print('Hasło nie składa się z cyfr i liter!')

if password.isalnum() and password.isupper():
    print('Hasło powinno zawierać małe litery')

if password.isalnum() and password.islower():
    print('Hasło powinno zawierać duże litery')
'''

