# map() - applies a function to every item in an iterable
# filter() - filters items based on a condition

# They are functions, so they take arguments:

# map(function, iterable)
# filter(function, iterable)


numbers = [1, 2, 3, 4, 5]
# Step 1: map() takes each item from numbers
# Step 2: Applies lambda x: x ** 2 to each
# Step 3: Returns a map object (iterator)
squared = map(lambda x: x ** 2, numbers)
# The comma separates:
# First argument: the function (lambda)
# Second argument: the iterable (numbers)
print(list(squared))  # [1, 4, 9, 16, 25]

# ================================================================================

# map	Built-in function	Applies a function to each item
# (	Function call start	Opening parenthesis for map()
# lambda x: x ** 2	Function argument	The function to apply to each item
# ,	Separator	Separates arguments to the map function
# numbers	Second argument	The list to iterate over
# )	Function call end	Closing parenthesis for map()

# ================================================================================

# now filter with lambda function
numbers = [1, 2, 3, 4, 5]
# Syntax: filter(condition_function, iterable)
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# =============================================================================

# filter	Built-in function that keeps items where condition is True
# lambda x: x % 2 == 0	Function that returns True for even numbers
# ,	Separates the two arguments
# numbers	The list to filter

# ==================================================================================

numbers = [1, 2, 3, 4, 5]
# filter() tests each item:
# 1 -> 1 % 2 == 0? False -> REJECTED
# 2 -> 2 % 2 == 0? True  -> KEPT
# 3 -> 3 % 2 == 0? False -> REJECTED
# 4 -> 4 % 2 == 0? True  -> KEPT
# 5 -> 5 % 2 == 0? False -> REJECTED
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)  # [2, 4]

# ====================================================================================

# why use list with map ?? 
numbers = [1, 2, 3, 4, 5]

# map() returns a MAP OBJECT (iterator), not a list
result = map(lambda x: x ** 2, numbers)
print(result)  # <map object at 0x...>

# Convert to list to see the values
result_list = list(result)
print(result_list)  # [1, 4, 9, 16, 25]

# You can also iterate directly
for value in map(lambda x: x ** 2, numbers):
    print(value)  # 1, 4, 9, 16, 25 (one by one)

# ========================================================================================

# Without list() - lazy evaluation
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)

# Nothing is calculated yet!
# It's like a "promise" to calculate when needed

print(squared)  # <map object at 0x...> (not the values)

# Now the calculation happens
for num in squared:
    print(num)  # 1, 4, 9, 16, 25

# After iterating once, the map is exhausted!
for num in squared:
    print(num)  # Nothing! The map is empty

# With list() - immediate calculation
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25] (values stored)

# ===========================================================================================

# without map and filter 

numbers = [1, 2, 3, 4, 5]

# 1. Traditional FOR LOOP - Explicit iteration
squared = []
for num in numbers:
    squared.append(num ** 2)
print(squared)  # [1, 4, 9, 16, 25]

# 2. MAP - Also iterates, but more concise
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# 3. LIST COMPREHENSION - Most Pythonic (for reference)
squared = [x ** 2 for x in numbers]
print(squared)  # [1, 4, 9, 16, 25]



