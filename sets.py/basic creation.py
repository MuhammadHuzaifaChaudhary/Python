# Empty set (MUST use set(), not {})
empty_set = set()
print(type(empty_set))  # <class 'set'>

# WARNING: {} creates an empty DICTIONARY, not a set!
empty_dict = {}
print(type(empty_dict))  # <class 'dict'>

# Set with elements
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
mixed = {1, "hello", 3.14, True}  # Can mix types

# From list (removes duplicates)
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = set(numbers)
print(unique)  # {1, 2, 3, 4}

# From string (unique characters)
text = "hello world"
chars = set(text)
print(chars)  # {'h', 'e', 'l', 'o', 'w', 'r', 'd'}

# c++ equivalent of set is unordered_set
#include <set>
#include <unordered_set>

# // Ordered set (tree-based)
# set<int> numbers = {1, 2, 3, 4, 5};

# // Unordered set (hash-based)
# unordered_set<int> fruits = {"apple", "banana", "cherry"};

# // No direct equivalent for mixed types