from delta import delta_calc

def answer():

    x1, x2, delta = delta_calc()
    if delta > 0:
        print(f'x_1 = {x1}, x_2 = {x2}')
    elif delta == 0:
        print(f'x1 = x2 = {x2} ')
    else:
        print("No results")


def main():
    answer()

if __name__ == '__main__':

    main()