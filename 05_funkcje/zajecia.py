'''

def my_mood(answear):
    print('My mood today: ')
    print(answear)


resp = input('how are you')
my_mood(resp)

'''



# 1,2,3
def add_book(books):
    title = input('Podaj ksiazke: ')
    grade = input(f'Ocen ksiazke {title}: ')
    books.append((title, grade))

def get_book(books):
    counter = len(books)
    while True:
        index = int(input('Podaj numer ksiazki: '))
        if index > counter or index < -counter:
            print('nie mamy tylu ksiazek na liscie')
        else:
            break
    index -= 1
    return books[index]

books = [('AAA', '3'), ('BBB', '4'), ('CCC', '5')]
#num = int(input('Ile ksiazek chcesz dodac: '))
#for _ in range(num):
#    add_book(books)
#print(books)

result = get_book(books)
print('Twoja ksiazka to: ', result)

