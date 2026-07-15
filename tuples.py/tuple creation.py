# Empty tuple
empty_tuple = ()
empty_tuple2 = tuple()

# Tuple with one element (note the comma!)
single = (5,)  # IMPORTANT: comma needed!
single2 = 5,   # Also works!
not_a_tuple = (5)  # This is just an int!

print(type(single))      # <class 'tuple'>
print(type(not_a_tuple)) # <class 'int'>

# Tuple with multiple elements
numbers = (1, 2, 3, 4, 5)
fruits = ("apple", "banana", "cherry")
mixed = (1, "hello", 3.14, True, [1, 2])  # Can mix types!

# Tuple without parentheses (tuple packing)
coordinates = 10, 20, 30
print(coordinates)  # (10, 20, 30)

# From list
my_list = [1, 2, 3]
my_tuple = tuple(my_list) 
# converting list to tuple
print(my_tuple)  # (1, 2, 3)

# From string
char_tuple = tuple("hello")
print(char_tuple)  # ('h', 'e', 'l', 'l', 'o')
# ===========================================================
#  C++ equivalent 
# ========================================================
# // C++ doesn't have a direct tuple equivalent with mixed types
# // But C++17 has std::tuple (still different)

# #include <tuple>
# #include <string>

# // Fixed-size tuple with mixed types
# tuple<int, string, double> t = make_tuple(1, "hello", 3.14);

# // Access elements (less convenient)
# cout << get<0>(t) << endl;  // 1
# cout << get<1>(t) << endl;  // hello