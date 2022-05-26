
#-----------------jeszcze nie działa--------------------

def is_even(i):
        if i % 2 == 0:
            print('Jest parzysta')
        else:
            print('Jest nieparzysta')

def main():

    i = input('Podaj liczbe')
    i = i.split(', ')
    print(type(i))
    i_leng = len(i)
    print(i_leng)

    for itm in i:
        print(f'{i}: ')
        is_even(i)

main()
