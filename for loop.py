# // C++: Initialization, condition, increment
# for (int i = 0; i < 5; i++) {
#     cout << i << endl;
# }
# // Output: 0 1 2 3 4

# in python 
# Python: Iterates over a range
# using range() function
for i in range(5):
    print(i)
# Output: 0 1 2 3 4

# Range with one parameter: range(stop)
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Range with two parameters: range(start, stop)
for i in range(2, 6):
    print(i)  # 2, 3, 4, 5

# Range with three parameters: range(start, stop, step)
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# Count backwards
for i in range(5, 0, -1):
    print(i)  # 5, 4, 3, 2, 1



    # Lists
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    for i in fruit:
        print(i) # a, p, p, l, e ... b, a, n, a, n, a ... c, h, e, r, r, y

# Strings (iterates over characters)
name = "Python"
for char in name:
    print(char)  # P, y, t, h, o, n

# Tuples
coordinates = (10, 20, 30)
for coord in coordinates:
    print(coord)

# Dictionaries
person = {"name": "John", "age": 30, "city": "NYC"}

# Iterate over keys
for key in person:
    print(key)  # name, age, city

# Iterate over values
for value in person.values():
    print(value)  # John, 30, NYC

# Iterate over key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")

word="hello"
for i in word:
    print(i) # h, e, l, l, o

# if we want gto iterate like C++ we can use range and len function to iterate over the string
for i in range(len(word)):
    print(word[i]) # h, e, l, l, o

    