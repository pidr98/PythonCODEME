class Dog():
    def __init__(self, name, color, race):
        self.name = name
        self.color = color
        self.race = race

    def how(self):
        print(f'{self.name} - How How')

    def tail_whip(self):
        return f'{self.name} whips his tail'

tuptus = Dog('Tuptus', 'black', 'Jamnik')
benek = Dog('Benek', 'Grey', 'Kundel')
tuptus.how()
print(benek.tail_whip())