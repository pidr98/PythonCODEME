
hobbits = ["Frodo", "Sam"]
grades = [1,2]

c = hobbits+grades
print(c)

print(hobbits[1])

hobbits[1] = 'frodo'
print(hobbits)

print('---------------------------------------')
print('---------------------------------------')

#praca z dokumentacją

tab = ['2', '1', '3', '7']
tab2 = tab.copy()
print('tab: ', tab)
print('tab2: ', tab2)

print('-----')

tab = ['2', '1', '3', '7']
tab.sort()
print(tab)

print('-----')

tab = ['2', '1', '3', '3', '7']
print(tab.count('3'))

print('-----')

tab.clear()
print(tab)

print('-----')
tab = [2, 1, 3, 7]
suma = sum(tab)
print(suma)

print('---------------------------------------')
print('---------------------------------------')

numbers = [1, 2, 3, (10, 20), 4, 5]
counter = 0
for n in numbers:
  if isinstance(n, tuple):
      break
  counter += 1
print('Wynik:', counter)

print('-----')

