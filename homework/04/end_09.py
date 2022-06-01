# 9. 5 użytkowników poproś o podanie 4 przedmiotów szkolnych, sprawdź czy przedmioty powtarzają się na listach.
# Wyświetl najpopularniejszy przedmiot.
# (Uwzględnij fakt, że użytkownicy mogą zapisać przedmioty małymi, drukowanymi lub zaczynając od dużej litery)

user1 = input('1. Podaj 4 przedmioty szkolne przedzielone spacją: ')
user2 = input('2. Podaj 4 przedmioty szkolne przedzielone spacją: ')
user3 = input('3. Podaj 4 przedmioty szkolne przedzielone spacją: ')
user4 = input('4. Podaj 4 przedmioty szkolne przedzielone spacją: ')
user5 = input('5. Podaj 4 przedmioty szkolne przedzielone spacją: ')
user1 = user1.split()
user2 = user2.split()
user3 = user3.split()
user4 = user4.split()
user5 = user5.split()


all_subjects = user1 + user2 + user3 + user4 + user5
for i in range(len(all_subjects)):
    all_subjects[i] = all_subjects[i].lower()

subject_counter = {}

print(all_subjects)
for subject in all_subjects:
    if subject in subject_counter:
        subject_counter[subject] += 1
    else:
        subject_counter[subject] = 1

max_value = None
for k, v in subject_counter.items():
    if max_value is None or v > max_value:
        sub = k
        max_value = v

print(sub, max_value)

