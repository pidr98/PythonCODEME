import random

def get_word():
    animals = ['cat', 'dog', 'bird']
    fruit = ['orange', 'banana', 'apple']
    word_animals = random.choice(animals)
    word_fruit = random.choice(fruit)
    question_type = int(input('0 = animals, 1 = fruit: '))

    if question_type == 0:
        word = word_animals
    else:
        word = word_fruit

    return word.lower()