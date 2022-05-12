#test
#------------
txt = "Mata"
#txt2 = txt.replace('M', 't')
#print(txt2)
#------------

# praca z dokumentacją
# zadanie 1
print('zad1')
print(txt.isdigit())
print('----------------')

# zadanie 2
print('zad2')
print(txt.center(20,'*'))
print('----------------')

# Zadanie 3
print('zad3')
txt3 = txt.rstrip('at')
print(txt3)
print('----------------')

# Zadanie 4
print('zad4')
txt4 = txt.isalpha() and (not txt.islower() and not txt.isupper())
print(txt4)
print('-----------------')

# zadanie 5
print('zad5')
banana = 'banana'
counter = banana.count('na')
print(counter)





