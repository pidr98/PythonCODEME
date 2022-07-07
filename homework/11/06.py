class Pracownik:
    def __init__(self, name, surname, salary, position, seniority, student):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.position = position
        self.seniority = seniority
        self.student = student

    def show_worker(self):
        print('Worker: ', self.name, self.surname, self.salary, self.position, self.seniority, self.student)

    def salary_rise(self):
        salary_after_rise = self.salary + self.salary * (self.seniority * 0.2)
        if self.student == False:
            salary_after_tax = salary_after_rise - ((salary_after_rise * 0.23) + (salary_after_rise * 0.08))
        else:
            salary_after_tax = salary_after_rise - (salary_after_rise * 0.23)

        print('Salary before rise: ', self.salary)
        print('Salary after rise: ', salary_after_rise, 'zł')
        print('Salary after tax: ', salary_after_tax, 'zł')

    def emails(self):
        name_consonant = [c for c in self.name if c not in "aeiouAEIOU "]
        surname_consonant = [c for c in self.surname if c not in "aeiouAEIOU "]
        email = name_consonant + surname_consonant
        print('Email: ', ''.join(map(str, email)).lower(), '@superemail.com')


worker1 = Pracownik('Jacek', 'Kowalski', 6000, 'programmer', 3, True)
worker1.show_worker()
worker1.salary_rise()
worker1.emails()
