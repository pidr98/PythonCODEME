def show_month(month_name, month_days):
    print('\n', month_name)

    for index, day in enumerate(month_days):
        if day < 10:
            day = '0' + str(day)

        if (index+1) % 7 == 0:
            print(day)

        else:
            print(day, end=' ')

def main():
    data = [
        ('January', range(31)),
        ('February', range(28)),
        ('March', range(31)),
        ('April', range(30)),
        ('May', range(31)),
        ('June', range(30)),
        ('July', range(31)),
        ('August', range(31)),
        ('September', range(30)),
        ('October', range(31)),
        ('November', range(30)),
        ('December', range(31)),
          ]

    data = dict(data)

    for name, days in data.items():
        show_month(name, days)


main()