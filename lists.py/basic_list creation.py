
# Empty list
empty_list = [] # no 1 way 
empty_list2 = list() # no 2 way 

# List with elements
numbers = [1, 2, 3, 4, 5]

print(numbers)  # [1, 2, 3, 4, 5]

fruits = ["apple", "banana", "cherry"]

print(fruits)  # ['apple', 'banana', 'cherry']

mixed = [1, "hello", 3.14, True, [1, 2]]  # Different types allowed!

print(mixed)  # [1, 'hello', 3.14, True, [1, 2]]

# List from range
numbers = list(range(5))  # [0, 1, 2, 3, 4]
numbers = list(range(1, 6))  # [1, 2, 3, 4, 5]
numbers = list(range(0, 10, 2))  # [0, 2, 4, 6, 8]

# List from string
chars = list("hello")  # ['h', 'e', 'l', 'l', 'o']
words = "hello world".split()  # ['hello', 'world']
print(words)

# in c++ 
# // C++ Array (fixed size)
# int arr[5] = {1, 2, 3, 4, 5};

# // C++ Vector (dynamic)
# #include <vector>
# vector<int> numbers = {1, 2, 3, 4, 5};
# vector<string> fruits = {"apple", "banana", "cherry"};

# // C++ can't mix types in one container
# // vector<int> mixed = {1, "hello", 3.14};  // ❌ ERROR!


