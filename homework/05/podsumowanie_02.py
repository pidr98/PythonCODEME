#2.
def minimum_of(a, b, c):
    if a > c and b > c:
        return c
    elif b > a and c > a:
        return a
    else:
        return b

def main():
    result = minimum_of(8,6,7)
    print(result)

main()