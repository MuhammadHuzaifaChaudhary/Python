# List to tuple
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(my_tuple)  # (1, 2, 3, 4, 5)

# Tuple to list
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
print(my_list)  # [1, 2, 3, 4, 5]

# Tuple to string
my_tuple = ('h', 'e', 'l', 'l', 'o')
my_string = ''.join(my_tuple)
print(my_string)  # hello