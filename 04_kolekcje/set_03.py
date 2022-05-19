tuple_1 = ('a', 'b','c', 'd', 'e', 'f')
tuple_2 = ('1', '2','3', '4', '5', '6','1','1',)

print(tuple_1[::2])
print(tuple_2[1::2])

tuple_3 = tuple_1[::2] + tuple_2[1::2]
lista = list(tuple_3)
print(lista)

result = set(lista)
print(result)