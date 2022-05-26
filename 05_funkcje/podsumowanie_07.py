#7.Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z Visą, MasterCard, a może AmericanExpress.
#Co wiemy o tych numerach tych kart?

#All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
#MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720. All have 16 digits.
#American Express card numbers start with 34 or 37 and have 15 digits.

def is_card(number):
    return number.isdigit() and 13 <= len(number) <= 16



def is_visa(number):
    if len(number) in [13, 16] and number[0] == '4':
        return True
    else:
        return False


def is_mastercard(number):
    if len(number) == 16 and (51 <= int(number[0:2]) <=55 or 2221 <= int(number[0:4]) <= 2720):
        return True
    else:
        return False


def is_american_express(number):
    return len(number) == 15 and number.startswith(('34', '37'))



def main():
#    number = '377451978681732'
    while True:
        number = input('Podaj nr karty: ').replace(' ', '')
        if is_card(number):
            break
        else:
            print('To nie jest poprawny numer karty')


    is_card(number)
    if is_visa(number):
        print('Visa', is_visa(number))
    if is_mastercard(number):
        print('MasterCard', is_mastercard(number))
    if is_american_express(number):
        print('AmericanExpress', is_american_express(number))
    pass

main()