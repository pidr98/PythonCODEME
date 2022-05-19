numbers = (2, 3, 5, 1, 7, 6)
x = input('Podaj liczbe od 1 do 10: ')
flag = False

for i, n in enumerate(numbers):
    if int(x) == n:
        print('znalazlem, pod indexem: ', i)
        flag = True
        break

if flag == False:
    print('nie ma takiej liczby')