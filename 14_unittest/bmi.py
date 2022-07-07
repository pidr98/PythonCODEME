class Bmi:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def calculate(self):
        return round(self.weight / self.height ** 2)



bmi = Bmi(60, 1.67)
print(bmi.calculate())