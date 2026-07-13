# f string is also used to format the string in python and
# it is more efficient than + operator to concatenate the string and variable.
name = "Alice"
age = 25
height = 1.75

# 1. Basic
print(f"Name: {name}, Age: {age}")

# 2. Expressions inside {}
print(f"Next year: {age + 1}")
print(f"Name in uppercase: {name.upper()}")

# 3. Formatting numbers
print(f"Height: {height:.2f}")  # 1.75
print(f"Height: {height:.1f}")  # 1.8
print(f"Percentage: {0.75:.1%}")  # 75.0%

# 4. Padding and alignment
print(f"{name:>10}")   # Right align (     Alice)
print(f"{name:<10}")   # Left align (Alice     )
print(f"{name:^10}")   # Center align (  Alice   )

# 5. Dictionary access
person = {"name": "Bob", "age": 30}
print(f"{person['name']} is {person['age']}")

# 6. Function calls
print(f"Length of name: {len(name)}")

# 7. Multi-line f-strings
message = f"""
Name: {name}
Age: {age}
Height: {height:.2f}m
"""
print(message)

# 8. Debugging (Python 3.8+)
x = 10
print(f"{x = }")  # Prints: x = 10


#  any operation can be done inside the f string like addition, subtraction, multiplication, division, etc.
# Anything inside {} is evaluated/executed
print(f"{2 + 2}")           # 4
print(f"{5 * 3}")           # 15
print(f"{10 / 2}")          # 5.0
print(f"{2 ** 10}")         # 1024


text = "hello world"
print(f"{text.replace('world', 'Python')}")  # hello Python
print(f"{text.split()}")                     # ['hello', 'world']
print(f"{text.upper().lower()}")             # hello world