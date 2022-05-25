#4.Napisz skrypt, który podaną listę podzieli na 3 równe listy i odwraca każdą z tych.

input_list = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]

list_one_third = len(input_list) / 3

result = []
temp = []

list_size = list_one_third

for i in input_list:
    list_size -= 1

    temp.append(i)

    if list_size == 0:
        temp.reverse()
        result.append(temp)

        list_size = list_one_third
        temp = []


for r in result:
    print(r)