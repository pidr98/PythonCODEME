#5.Napisz grę ciepło - zimno tak, aby korzystać z funkcji.
import random

def cieplo_zimno(losulosu, i):
    while i < 6:
        user_input = int(input('Podaj cyfrę: '))
        if user_input == losulosu:
            print("Zgadłeś!")
            break
        elif user_input < losulosu:
            if (user_input - losulosu) < 10:
                print('Ciepło')
            else:
                print('Zimno')
            print('Za nisko')
            i += 1
            print('Pozostałe próby: ', 6 - i)
            continue
        else:
            if (user_input - losulosu) < 10:
                print('Ciepło')
            else:
                print('Zimno')
            print('Za wysoko')
            i += 1
            print('Pozostałe próby: ', 6 - i)
            continue

    print('\n----------Koniec----------')



def main():
    losulosu = random.randint(1, 100)
    i = 0

    cieplo_zimno(losulosu, i)

main()
