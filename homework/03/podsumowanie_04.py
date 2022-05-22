import random

rounds = int(input('liczba rund: '))

losu = ['k', 'p', 'n']
cpu_score = 0
user_score = 0
i = 0

while i < rounds:
    user_input = input('\n(k)amień, (p)apier (n)ozyce: ')
    print('')
    if user_input == 'koniec':
        quit()

    losulosu = random.choice(losu)

    if user_input == losulosu:
        print('Komputer wybrał: ', losulosu, '\nTy wybrałeś/aś:', user_input)
        print('Remis')
        print('Komputer: ', cpu_score,'Ty: ', user_score)
        i += 1
        continue
    elif (user_input == 'k' and losulosu == 'p') or (user_input == 'p' and losulosu == 'n') or (user_input == 'n' and losulosu == 'k'):
        cpu_score += 1
        print('Komputer wybrał: ', losulosu, '\nTy wybrałeś/aś:', user_input)
        print("Komputer wygrał :( ")
        print('Komputer: ', cpu_score, 'Ty: ', user_score)
        i += 1
        continue
    else:
        user_score += 1
        print('Komputer wybrał: ', losulosu, '\nTy wybrałeś/aś:', user_input)
        print('Wygrałeś!')
        print('Komputer: ', cpu_score, 'Ty: ', user_score)
        i += 1
        continue
print('\n----------Koniec----------')