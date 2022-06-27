from fibon_mod import fibon

def main():
    n = int(input("How many terms? "))

    n1, n2 = 0, 1
    count = 0
    fibon(n, n1, n2, count)

if __name__ == '__main__':
    main()
