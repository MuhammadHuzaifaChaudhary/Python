# Tuples are not sortable directly (no sort method)
numbers = (5, 2, 8, 1, 9, 3)

# Convert to list, sort, convert back
sorted_tuple = tuple(sorted(numbers))
print(sorted_tuple)  # (1, 2, 3, 5, 8, 9)

# Or use sorted() which returns list
sorted_list = sorted(numbers)
print(sorted_list)  # [1, 2, 3, 5, 8, 9]

# Sorting list of tuples
students = [("Alice", 25), ("Bob", 22), ("Charlie", 28)]
students.sort(key=lambda x: x[1])  # Sort by age
print(students)  # [('Bob', 22), ('Alice', 25), ('Charlie', 28)]