def calculate_bmi(weight, height):
    return round(weight / height ** 2)


def get_bmi(bmi):
    if bmi <= 18.49:
        return 'Niedowaga'
    elif bmi >= 18.50 and bmi <= 24.99:
        return 'Waga prawidłowa'
    elif bmi >= 25 and bmi <= 29.99:
        return 'Nadwaga'
    elif bmi >= 30:
        return 'Otyłość'
    else:
        return 'Błąd'


def main():
    wei = float(input("Podaj wagę w kg: "))
    hei = float(input("Podaj wzrost w metrach: "))

    result = calculate_bmi(wei, hei)
    print('Twoje BMI: ', get_bmi(result))

main()
