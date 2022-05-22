#2. Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.

digits = input('Podaj 10 liczb przedzielone spacją: ')
digits = digits.split()

for num in digits:
    if (int(num) % 2) == 1:
        print(num, end='')

