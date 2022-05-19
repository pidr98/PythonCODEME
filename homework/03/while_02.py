# 2.Napisz prostą grę, w której użytkownik musi zgadnąć liczbę od 0 - 20 ukrytą w programie (np. secret_num = 5).
# Pytaj użytkownika o podanie liczby tak długo, aż nie zgadnie.

secret_num = 5
while True:
    x = int(input('Podaj liczbę: '))
    if x == secret_num:
        print('Gratulacje')
        break
    else:
        print('Jeszcze raz')

