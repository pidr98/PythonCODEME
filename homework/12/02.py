class UsefulStuff:
    def __init__(self, name):
        print(name, 'is very useful')


class Cat(UsefulStuff):
    def __init__(self, cats):
        print(cats, "Cat")
        super().__init__(cats)


class Dog(UsefulStuff):
    def __init__(self, dogs):
        print(dogs, "Dog")
        super().__init__(dogs)


class Human(UsefulStuff):
    def __init__(self, humans):
        print(humans, "Human")
        super().__init__(humans)


class Animals(UsefulStuff):
    def __init__(self, Animal):
        print(Animal, "Animals")
        super().__init__(Animal)


class Ssaki(Cat, Dog, Human):
    def __init__(self):
        print('Ssaki')
        super().__init__('Ssaki')


animl = Animals(Ssaki)
print(Animals.__mro__)