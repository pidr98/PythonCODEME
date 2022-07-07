class Storczyk():
    def __init__(self, species, color, bloom, kingdom):
        self.species = species
        self.color = color
        self.bloom = bloom
        self.kingdom = kingdom

    def met1(self):
        print(f'{self.species} - {self.color}, {self.bloom}, {self.kingdom}')

    def met2(self):
        return f'{self.species} - {self.color}, {self.bloom}, {self.kingdom}'

storczyk1 = Storczyk('Gatunek1', 'bialy', 'wiosna', 'krolestwo roslin')
storczyk2 = Storczyk('Gatunek2', 'niebieski', 'wiosna', 'krolestwo roslin')
storczyk3 = Storczyk('Gatunek3', 'rozowy', 'lato', 'krolestwo roslin')


storczyk1.met1()
print(storczyk2.met2())
storczyk3.met1()