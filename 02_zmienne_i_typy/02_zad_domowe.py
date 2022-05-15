# Liczby
# 2.Zmodyfikuj skrypt tak, by przyjmował wartości od użytkownika.
'''
fuel_consumption = float(input("Spalanie: "))
distance = float(input("Dystans: "))
fuel_price = float(input("Cena paliwa za L: "))

travel_cost = (fuel_consumption * distance) / 100 * fuel_price
print('Koszt wyprawy wynosi: ', travel_cost)
'''
# Bool
# 5.Czy 43 - 13 będzie się równać 11 + 12 ?
'''
a = 43 - 13
b = 11 + 12
print (a == b)
'''
# 6.Czy dzielenie 129 przez 17 bez reszty wynosi 3?
'''
print( (129 / 17) == 3)
'''
# 7.Czy 247 podzielone przez 5 daje resztę 2?
'''
print(247 % 5 == 2)
'''

# String
# 2.Stwórz dwie zmienne s1 i s2 przechowujące dowolne wyrazy, utwórz nowy łańcuch s3, dołączając s2 w środku s1.
'''
s1 = 'pierwszy'
s2 = 'DRUGI'
s3 = s1[:4] + s2 + s1[4:]
print(s3)
'''

# 4.Utwórz skrypt, który zapyta użytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:
'''
book_title = input('Tytuł książki: ')
auth_surname = input('Nazwisko autora: ')
pages = input('Liczba stron: ')

# -Sprawdź czy tytuł i nazwisko składają się tylko z liter, natomiast liczba stron jest wartością liczbową.
print('Czy tytuł zawiera cyfry:', book_title.isnumeric())
print('Czy nazwisko zawiera cyfry:' ,auth_surname.isnumeric())
print('Czy liczba stron jest wartością liczbową:' ,pages.isnumeric())

# -Użytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery – popraw ich
print('Tytuł:', book_title.title())
# -Połącz dane w jeden ciąg book za pomocą spacji
book = 'Tytuł:' + book_title.title() + ' Autor:' + auth_surname + ' Liczba stron:' + pages
print(book)
# -Policz liczbę wszystkich znaków w napisie book
print('znaki w book:', len(book))

'''

# 5.Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej np.: Kobyła ma mały bok.
#   Pozwól użytkownikowi wprowadzić dowolne zdanie. Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.
'''
c = input('Zdanie:')
c = c.replace(' ', '')
c = c.lower()
print(c)
d = c[::-1]
print(d)
print(c == d)
'''

# 6.Przekopiuj zawartość import this do zmiennej.
t = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

# -Policz liczbę wystąpień słowa better.
print('Ilość better:',t.count('better'))
# -Usuń z tekstu symbol gwiazdki

print(t.replace('*', ''))
# -Zamień jedno wystąpienie explain na understand
print(t.replace('explain', 'understand', 1))
# -Usuń spacje i połącz wszystkie słowa myślnikiem
print(t.replace(' ', '-'))
# -Podziel tekst na osobne zdania za pomocą kropki

