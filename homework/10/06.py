def main():
    n = int(input('Input number: '))

    for i in range(1, n + 1):
        for j in range(0, n - i + 1):
            print(' ', end='')

        first_number = 1
        for j in range(1, i + 1):
            print(' ', first_number, sep='', end='')

            first_number = first_number * (i - j) // j
        print()

if __name__ == '__main__':
    main()