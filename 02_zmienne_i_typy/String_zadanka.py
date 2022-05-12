# ------Zadanka------
# Zadanie 1
#Stwórz zmienną przechowującą wyraz o długości nieparzystej większej niż 7 i zwróć łańcuch złożony z trzech środkowych znaków danego ciągu.

word = 'dlugieslowo'
print('Zadanie 1')
print(word[5])

print(len(word))
print(len(word)//2)

mid_index = len(word)//2

prev_id = mid_index -1
print(prev_id)
next_id = mid_index +1
print(next_id)

print(word[prev_id] + word[mid_index] + word[next_id])
print(word[prev_id:next_id + 1])
print('------------')

#Zadanie 2
print('Zadanie 2')

print('------------')

#Zadanie 3
print('Zadanie 3')
quote = 'Honesty is the first chapter in the book of wisdom.'
#1
print('Liczba liter: ', len(quote))
#2
print(quote[-7:-1])
#3
id_half = len(quote)//2
print(quote[:id_half+1])
#4
print(quote[-1])
#5
print(quote[id_half::3])
#6
print(quote[::2])
#7
print(quote[::-1])
#8
new_quote = quote.replace('wisdom', 'friendship')
print(new_quote)

print('-------------')
