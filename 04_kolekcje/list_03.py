digits = input('Podaj liczby przedzielone przecinkiem: ')
digits = digits.split(', ')
print(digits)

print('Czy pierwszy = ostatni: ', digits[0], digits[-1])

if digits[0] == digits[-1]:
    print('Są takie same')
else:
    print('Są inne')
