# Basic set comprehension
squares = {x**2 for x in range(10)}
print(squares)  # {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# With condition
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0, 4, 16, 36, 64}

# From a string
vowels = {'a', 'e', 'i', 'o', 'u'}
text = "hello world"
vowels_in_text = {char for char in text if char in vowels}
print(vowels_in_text)  # {'e', 'o'}

# Complex transformation
names = ["Alice", "Bob", "Charlie", "David"]
first_letters = {name[0] for name in names}
print(first_letters)  # {'A', 'B', 'C', 'D'}