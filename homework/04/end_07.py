#7.Usuń duplikat z podanej list i utwórz na jej bazie krotkę. Znajdź minimalną i maksymalną liczbę w krotce.

example_list = [34, 17, 25, 41, 12, 194, 41, 3, 12, 99, 94]

example_list = list(dict.fromkeys(example_list))

print(example_list)

tuple1 = tuple(example_list)

tuple1_min = min(tuple1)
tuple1_max = max(tuple1)

print('min:', tuple1_min,'max:', tuple1_max)