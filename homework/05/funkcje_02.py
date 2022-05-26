def is_even(i):
    if i % 2 == 0:
        print('Jest parzysta')
    else:
        print('Jest nieparzysta')

def main():
    i = float(input('Podaj liczbe'))
    is_even(i)
main()