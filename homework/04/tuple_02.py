# 2. Stwórz krotkę. Znajdź powtarzające się elementy krotki. Wyświetl je.

tuple1 = (1,2,3,3,4,5,8,1)

duplicates = list(set([i for i in tuple1 if tuple1.count(i) > 1]))

print(duplicates)
