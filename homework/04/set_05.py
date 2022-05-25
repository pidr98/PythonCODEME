#5. Porównaj zachowanie discard() vs remove() dla typu set.

set1 = set([10,11,12,13,14,15])
set2 = set([10,11,12,13,14,15])

set1.discard(11)
print(set1)
set2.remove(1)
print(set2)

# remove usuwa element z listy jeśli istnieje, inaczej wywali błąd
# discard usuwa element z listy  jeśli istnieje, w przeciwnym wypadku po prostu drukuje cały set
