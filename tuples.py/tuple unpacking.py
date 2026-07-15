# Tuple with multiple values
coordinates = (10, 20, 30)

# Unpack into variables
x, y, z = coordinates
print(x)  # 10
print(y)  # 20
print(z)  # 30

# Swap variables (Python magic!)
a = 5
b = 10
a, b = b, a  # Swaps values!
print(a)  # 10
print(b)  # 5

# Multiple assignment
name, age, city = "Alice", 25, "NYC"
print(name)  # Alice
print(age)   # 25
print(city)  # NYC

# ==========================================================
# extended unpacking with * 
# ==========================================================

numbers = (1, 2, 3, 4, 5)

# Unpack with * (rest operator)
first, *middle, last = numbers
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5

# Another example
first, second, *rest = numbers
print(first)   # 1
print(second)  # 2
print(rest)    # [3, 4, 5]

# Ignoring values with _
*_, last = numbers  # Ignore all except last
print(last)  # 5

first, *_, last = numbers
print(first)  # 1
print(last)   # 5

