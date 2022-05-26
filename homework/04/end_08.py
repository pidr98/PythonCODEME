#8.Utwórz słownik dla 10 krajów Europy zawierajacy listy 10 najpopularniejszych imion żeńskich.
# Zapisz imiona w wersji anglojęzycznej.
# Dodaj wszystki listy razem.
# Nowa lista powinna zawierać 100 elementów.
# Wyświetl tylko te imiona, które wystąpiły conajmniej w 3 krajach.
import collections

# nie wiem.

germany_names = ['Mia', 'Emma', 'Sofia', 'Hanna', 'Emilia', 'Anna', 'Marie', 'Lina', 'Lea', 'Lena']
france_names = ['Elea', 'Lya', 'Elyna', 'Anna', 'Lili', 'Noemie', 'Sophia', 'Julia', 'Louise', 'Ella']
italy_names = ['Sofia', 'Aurora', 'Giulia', 'Ginevra', 'Alice', 'Emma', 'Giorgia', 'Beatrice', 'Greta', 'Vittoria']
gb_names = ['Olivia', 'Amelia', 'Isla', 'Ava', 'Mia', 'Ivy', 'Lily', 'Isabella', 'Rosie', 'Sophia']
poland_names = ['Anna', 'Katarzyna', 'Maria', 'Małgorzata', 'Agnieszka', 'Barbara', 'Ewa', 'Magdalena', 'Elżbieta', 'Krystyna']
netherlands_names = ['Emma', 'Julia', 'Mila', 'Tess', 'Sophie', 'Zoe', 'Sara', 'Nora', 'Yara', 'Eva']
ukraine_names = ['Natasha', 'Anastasia', 'Kristina', 'Darya', 'Yulia', 'Sasha', 'Maria', 'Sofia', 'Victoria', 'Anna']
sweden_names = ['Anna', 'Eva', 'Maria', 'Karin', 'Sara', 'Kristina', 'Lena', 'Emma', 'Kerstin', 'Marie']
norway_names = ['Anne', 'Inger', 'Kari', 'Marit', 'Ingrid', 'Liv', 'Maria', 'Ida', 'Eva', 'Anna']
finland_names = ['Aino', 'Olivia', 'Sofia', 'Pihla', 'Aada', 'Eevi', 'Isla', 'Lilja', 'Helmi', 'Ellen']


full_names = germany_names + france_names + italy_names + gb_names + poland_names + netherlands_names + ukraine_names + sweden_names + norway_names + finland_names
dict_names = dict(germany_names)
print(full_names)
print(len(full_names))
print(type(full_names))

occurance = collections.Counter(full_names)
print(occurance)



