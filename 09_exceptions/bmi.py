def calc_bmi(height, weight):
    return round(weight / height ** 2, 2)


def get_bmi_status(bmi):
    if bmi < 18.5:
        return "underweight.txt"
    elif bmi < 25:
        return "standard.txt"
    elif bmi < 30:
        return "overweight.txt"
    else:
        return "obesity.txt"