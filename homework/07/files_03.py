N = 5
with open("cytaty.txt", encoding='UTF-8') as file:
    for i in range(N):
        line = next(file).strip()
        print(line)