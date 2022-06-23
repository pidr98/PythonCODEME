class Student():
    def __init__(self, first, last, age, email):
        self.first = first
        self.last = last
        self.age = age
        self.email = email

anna = Student('Anna', 'Kowalska', 23, 'a.kowalska@university.com')

print(anna.last, anna.first, anna.age)