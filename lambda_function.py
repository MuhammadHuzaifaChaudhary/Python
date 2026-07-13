# lambda then variable name then : then expression 

# Simple lambda
add = lambda a, b: a + b
print(add(5, 3))  # 8

# Lambda with one parameter
square = lambda x: x ** 2
print(square(5))  # 25

# Lambda as function argument
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Lambda with filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]

# Lambda with sorting
people = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]
people.sort(key=lambda person: person[1])  # Sort by age
print(people)  # [('Charlie', 20), ('Alice', 25), ('Bob', 30)]

