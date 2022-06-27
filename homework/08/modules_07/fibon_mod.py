def fibon(n, n1, n2, count):
    if n <= 0:
        print("Please enter a positive integer")

    elif n == 1:
        print("Fibonacci sequence up to", n, ":")
        print(n1)

    else:
        print("Fibonacci sequence:")
        while count < n:
            print(n1)
            nth = n1 + n2

            n1 = n2
            n2 = nth
            count += 1