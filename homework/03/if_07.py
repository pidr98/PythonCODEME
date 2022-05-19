#Rozwiń kod bmi.py z pierwszych zajęć
# dodając teraz instrukcję warunkową, która wyświetli w zależności od wyniku: niedowaga / waga normalna / nadwaga / otyłość.

weight = float(input("Podaj wagę w kg: "))
height = float(input("Podaj wzrost w metrach: "))

BMI = weight / height ** 2

print("Twoje BMI wynosi:",BMI)

if BMI <= 18.49:
    print('Niedowaga')
elif BMI >= 18.50 and BMI <= 24.99:
    print('Waga prawidłowa')
elif BMI >= 25 and BMI <=29.99:
    print('Nadwaga')
elif BMI >= 30:
    print('Otyłość')
else:
    print('Błąd')