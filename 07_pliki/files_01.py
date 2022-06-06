import random


def get_quote():
    with open('cytaty.txt', encoding='UTF-8') as fopen:
        content = fopen.readlines()

        quote = random.choice(content)
        return quote


def show(quote):
    quote = quote.strip('\n')
    lenght = len(quote) + 20

    print('Quote of the day is:')
    print('*' * lenght)
    print(quote.center(lenght))
    print('*' * lenght)


def main():
    quote = get_quote()
    show(quote)
main()
