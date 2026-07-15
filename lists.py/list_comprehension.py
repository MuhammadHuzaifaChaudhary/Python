# list comprehension basic syntax 
# [expression for item in iterable if condition]

# Create list of squares
squares = [x ** 2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Equivalent for loop
squares = []
for x in range(10):
    squares.append(x ** 2)
print(squares)  # Same result!

# With condition
evens = [x for x in range(20) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# With nested loops
pairs = [(x, y) for x in [1, 2, 3] for y in [4, 5, 6]]
print(pairs)  # [(1,4), (1,5), (1,6), (2,4), (2,5), (2,6), (3,4), (3,5), (3,6)]

# Complex transformation
numbers = [1, 2, 3, 4, 5]
doubled_odds = [x * 2 for x in numbers if x % 2 != 0]
print(doubled_odds)  # [2, 6, 10]

# With if-else
results = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(results)  # ['even', 'odd', 'even', 'odd', 'even']



# real world examples 
# Convert temperatures
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(c * 9/5) + 32 for c in celsius]
print(fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 104.0]

# Extract first letters
names = ["Alice", "Bob", "Charlie", "David"]
first_letters = [name[0] for name in names]
print(first_letters)  # ['A', 'B', 'C', 'D']

# Filter and transform
scores = [85, 92, 78, 65, 95, 88, 70]
passing_grades = [score + 5 for score in scores if score >= 70]
print(passing_grades)  # [90, 97, 83, 100, 93]