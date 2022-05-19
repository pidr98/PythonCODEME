txt = """Szybko, zbudź się, szybko, wstawaj Szybko, szybko, stygnie kawa Szybko, zęby myj i ręce"""
txt = txt.replace(',', '')
txt = txt.lower()
words = txt.split()

word_counter = {}

for word in words:
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1

for k, v in word_counter.items():
    print(f'- {k} : {v}')