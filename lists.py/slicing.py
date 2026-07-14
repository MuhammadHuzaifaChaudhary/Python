numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Basic slicing
print(numbers[2:6])     # [2, 3, 4, 5] (from index 2 to 5)
print(numbers[:5])      # [0, 1, 2, 3, 4] (from start to 4)
print(numbers[5:])      # [5, 6, 7, 8, 9] (from 5 to end)
print(numbers[:])       # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (copy)

# Slicing with step
print(numbers[0:10:2])  # [0, 2, 4, 6, 8] (every 2nd)
print(numbers[1:10:2])  # [1, 3, 5, 7, 9] (every 2nd from index 1)

# Negative step (reverse!)
print(numbers[::-1])    # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reverse)
print(numbers[8:2:-1])  # [8, 7, 6, 5, 4, 3]

# Negative indices in slicing
print(numbers[-5:-1])   # [5, 6, 7, 8]
print(numbers[-3:])     # [7, 8, 9]

# ===========================================================================
# list of strings 
# ===========================================================================
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

print(fruits[1:3])      # ['banana', 'cherry']
print(fruits[:2])       # ['apple', 'banana']
print(fruits[2:])       # ['cherry', 'date', 'elderberry']
print(fruits[::-1])     # ['elderberry', 'date', 'cherry', 'banana', 'apple']

# ==============================================================================
# slicing creates a new list and does not modify the original list.

original = [1, 2, 3, 4, 5]
sliced = original[1:4]  # [2, 3, 4]

# Modifying slice doesn't affect original
sliced[0] = 99
print(sliced)     # [99, 3, 4]
print(original)   # [1, 2, 3, 4, 5] (unchanged!)

# ==============================================================================
# // C++ - Slicing is not built-in, but can be done with iterators
