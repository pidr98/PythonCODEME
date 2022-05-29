#4. Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie.
# Powinna zwrócić komunikat: “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”.

def if_in_range(min, max):
    num = 5
    if min <= num and num <= max:
        print(f'Number {num} is in range')
    else:
        print('Not in range')

def main():
    min = int(input('Podaj zakres min: '))
    max = int(input('Podaj zakres max: '))

    if_in_range(min, max)

main()