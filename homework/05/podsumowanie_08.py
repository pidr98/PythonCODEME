#8.Napisz program, który będzie sprawdzał, czy nasz samochód kwalifikuje się do zarejestrowania jako zabytek.

def is_vintage(vintage_car):
    to_list = list(vintage_car.items())
    # print(to_list)

    year_car = to_list[2]
    year_car = year_car[1]
    # print(type(year_car))
    # print(year_car)

    name_car = to_list[0]
    name_car = name_car[1]
    # print(name_car)

    year = 2022

    if (year - year_car) >= 25:
        print(f'{name_car} jest zabytkiem')
    else:
        print(f'{name_car} nie jest zabytkowe')

def main():
    vintage_car = {'marka': 'ferrari', 'model': 'f40', 'rocznik': 1990}
    print(vintage_car)
    is_vintage(vintage_car)
main()