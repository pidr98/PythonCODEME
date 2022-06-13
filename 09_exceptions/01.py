numbers = [13, 'xd', 2.34]
for i in numbers:
  try:
    result = 10 / i
    print(result)
  except (ZeroDivisionError, ValueError):
    print(f'10/{i} Nie mozna wykonac')