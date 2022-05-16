'''
x = 5

if x > 4:
    print('pierwszy if')

if x == 3:
    print('drugi if')
elif x >= 0:
    print('elif')
else:
    print('else')
'''

'''
season = 'zima'
if season == 'wiosna':
    print('zasadź rośliny')
elif season == 'lato':
    print('podlewaj ogród')
elif season == 'jesien':
    print('zbierz owoce')
elif season == 'zima':
    print('brrr za zimno!')
else:
    print('nie ma takiej pory roku')
'''

'''
txt = "abrakadabra"

for letter in txt:
    print('- ', letter)


names = ["Ada", "Julia", "Ruby", "Perl"]

for step in names:
    print('Hello!', step)


for number in range(5, 20, 2):
    print('->', number)

print('----------------')
for index in range(4):
    print(index, names[index])

for index, elem in enumerate(txt):
    print(index, elem)
'''

'''
pa = ""
magic = "hokuspokus"
for num in range(2, 10, 2):
    pa = pa + str(num) + magic[num]
    print(pa)
'''


# 1. Stwórz listę przedmiotów, które zabierzesz na samotną wyprawę w góry. Wyświetl nazwę właśnie spakowanego przedmiotu, po ostatnim przedmiocie pokaż informację: “Great, we are ready!”
'''
items = ["bag", "tent", "mug"]

for i in items:
    print('-', i)
print('Great, we are ready!')
'''


# 3.Napisz program, który dla 10 kolejnych liczb naturalnych wyświetli sumę poprzedników. Oczekiwany wynik: 1, 3, 6, 10, 15, 21, 28, 36, 45, 55
'''
sum_num = 0
for num in range (1,11):
    sum_num = sum_num + num
    print(sum_num)
'''

'''
price = 15

while (price > 10):
    print(price, '$ - za drogo')
    price = price - 2

print(price, '$ super promocja!')
'''
# while
# 1.Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach. Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.
'''
temperature = 0
while temperature <= 200:
    c = 5/9 * temperature - 32
    print(temperature, c)
    temperature += 20
'''

#zadanie z przedmiotami szkolnymi i ocenami
'''
i = 0
while i <= 2:
    subject = input('Przedmiot szkolny: ')
    grade = input('Ocena w skali 1-6: ')
    wyswietl = subject + ': ' + grade
    print(wyswietl)
    i = i + 1
    continue
print("Koniec")
'''

# 1.Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem). Następnie powitaj każdą osobę na liście.
'''
names = 'anna, jan, krzysiek'
names = names.split(', ')

for n in names:
    print('Hello ', n)
'''
# 3.W podanym przez użytkownika ciągu wejściowym policz wszystkie małe litery, wielkie litery, cyfry i znaki specjalne.
txt = input('Podaj ciąg znaków: ')

count_num = 0
count_up = 0
count_low = 0
for l in txt:
    if l.isdigit():
        count_num += 1
        continue

    if l.isupper():
        count_up += 1
        continue

    if l.islower():
        count_low +=1

print(f'Text:{txt}')
print('Cyfry: ', count_num)
print('Duże litery: ', count_up)
print('Małe litery: ', count_low)

