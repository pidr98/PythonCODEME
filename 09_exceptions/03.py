def main():
  items = ['a', 'abc', 5, 5.5, [5, 3], (7, 8), 0, True,, False, None, {}]

  try:
    id = int(input('Podaj index: '))
    print(1 / items[id])
  except ValueError:
    print('Value Error')
  except TypeError:
    print('Type Error')
  except ZeroDivisionError:
    print('Zero Division Error')
  except IndexError:
    print(f'You should give lower value. 0 - {len(items) - 1}')

if __name__ == '__main__':
    main()