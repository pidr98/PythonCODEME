# 4.Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N (N podane przez użytkownika, ale nie większe niż 8).

x = int(input('Podaj liczbę nie większą niż 8: '))
silnia = 1

if x <= 8:
    for i in range(1, x+1):
        silnia = silnia * i
        print(f'{i}! =', silnia)

else:
    print('liczba większa od 8')