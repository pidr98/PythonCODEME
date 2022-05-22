import random

losulosu = random.randint(1,100)

i = 0

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

print('\n----------Przegrałeś----------')