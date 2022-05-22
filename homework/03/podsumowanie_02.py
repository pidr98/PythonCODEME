#2. Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych.
# Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).

txt = input('Podaj tekst: ')

out = []
for i in range(len(txt)):
    if i % 2 == 1:
        print(txt[i], end='')

slice_str = slice(1, len(txt), 2)
print(txt[slice_str])

