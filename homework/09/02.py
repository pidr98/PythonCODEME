test_tuple = (1, [5, 6, 4], 9, 10, 12, 13, 15, 20)
print("The original tuple : " + str(test_tuple))

try:
    tuple_index = int(input('Tuple index (0-2) : '))
    change_index = int(input('Input value: '))
    test_tuple[1][tuple_index] = change_index
except(ValueError, IndexError):
    print('Wrong input!')

print("The modified tuple : " + str(test_tuple))