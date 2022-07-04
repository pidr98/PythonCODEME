import random

def kpn(losu, cpu_score, user_score, i):
    rounds = int(input('liczba rund: '))

    while i < rounds:
        user_input = input('\n(k)amień, (p)apier (n)ozyce: ')
        if user_input == 'k' or user_input == 'p' or user_input == 'n':
            print('')
            if user_input == 'koniec':
                quit()

            losulosu = random.choice(losu)

            if user_input == losulosu:
                print('Komputer wybrał: ', losulosu, '\nTy wybrałeś/aś:', user_input)
                print('Remis')
                print('Komputer: ', cpu_score, 'Ty: ', user_score)
                i += 1
                continue
            elif (user_input == 'k' and losulosu == 'p') or (user_input == 'p' and losulosu == 'n') or (
                    user_input == 'n' and losulosu == 'k'):
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
        else:
            print('Wrong input')
    print('\n----------Koniec----------')

def main():
    losu = ['k', 'p', 'n']
    cpu_score = 0
    user_score = 0
    i = 0
    try:
        kpn(losu, cpu_score, user_score, i)
    except ValueError:
        print('Wrong input')
main()
