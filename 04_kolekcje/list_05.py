lista_2d = [
    ['Dorota', 'Wellman', 'Dziennikarka'],
    ['adam', 'malysz', 'sportowiec'],
    ['robert', 'lewy', 'pilkarz'],
    ['krystyna', 'czubowna', 'lektor']
]
for person in lista_2d:
    for id, value in enumerate(person):
        if id == 1:
            print( value, end=' -> ')
        else:
            print(value, end=' ')
    print()