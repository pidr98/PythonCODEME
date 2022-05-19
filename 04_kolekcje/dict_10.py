n = int(input('Podaj liczbę od 1 do 10: '))

dict_sqr = {}
for v in range(1, n + 1):
    dict_sqr[v] = v * v

print(dict_sqr)
