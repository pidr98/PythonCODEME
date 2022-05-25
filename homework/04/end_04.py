#4.Utworz tabliczkę mnożenia jako zagnieżdżoną listę o rozmiarze 10 x 10, wypełnioną wynikami mnożenia wiersz × kolumna.

num = 1

while True:
    if num <= 10:
        list1 = [num * i for i in range(1, 11)]
        print(list1)
        num += 1
    else:
        print(type(list1))
        print('Koniec')

        exit()