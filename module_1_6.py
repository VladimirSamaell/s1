my_dict = {'V': 2001, 'S': 2002, 'Q': 2003}
print(my_dict)
print(my_dict['V'])
print(my_dict.get('W', 'Такого ключа нет'))
my_dict.update({'F': 2004,
               'G': 2005,
               })
V = my_dict.pop('V')
print(V)
print(my_dict)

my_set = {1, 2, 3, 3, 2, 1, 'ss', 'ss', True}
print(my_set)
my_set.add(4)
my_set.add(5)
my_set.discard(1)
print(my_set)