# 2. Utwórz listę lub krotkę tuples_to_dict zawierającą krotki 2 elementowe. Przekształć ją w słownik dict_from_tuples.
tuple_to_dict = (
    ('cat', 'chat'),
    ('hat', 'chapeau'),
    ('potato', 'pomme de terre')
)
print(type(tuple_to_dict))
dict_from_list = dict(tuple_to_dict)

print(dict_from_list)
print(type(dict_from_list))
