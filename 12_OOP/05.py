from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def desc(self):
        pass

    @abstractmethod
    def licence(self):
        pass

class Bike(Vehicle):
    def __init__(self):
        print('create bike')

    def licence(self):
        return 'AM'

    def desc(self):
        return 'you can pass your bike'

def main():
    b = Bike()
    print(b.licence())

if __name__ == '__main__':
    main()