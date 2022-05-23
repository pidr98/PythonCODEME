#3.
def maximum_of(a, b, c):
    if a > b and b > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

def main():
    result = maximum_of(3,6,1)
    print(result)

main()