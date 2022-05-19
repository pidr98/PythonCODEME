# 6.Zapytaj użytkownika o numer od 1 do 100,
# jeśli użytkownik zgadnie liczbę ukrytą przez programistę wyświetl komunikat “gratulacje!”,
# w przeciwnym razie wyświetl “pudło!”.
import random

rand = random.randint(0, 100)
num = int(input('Wpisz cyfrę od 1 do 100:'))
print(rand)
if rand is not num:
    print('Pudło')
else:
    print(f'Gratulacje, cyfra to {rand} ')