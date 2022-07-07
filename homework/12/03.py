class UsefulStuff:
    def __init__(self, name):
        print(name, 'is used to make life easier!')


class Pen(UsefulStuff):
    def __init__(self, pen):
        print(pen, "pen")
        super().__init__(pen)


class Pinapple(UsefulStuff):
    def __init__(self, pinapple):
        print(pinapple, "pineapple")
        super().__init__(pinapple)


class PenPinapple(Pen, Pinapple):
    def __init__(self):
        print('penpineapple')
        super().__init__('PENPINEAPPLE')


pp = PenPinapple()