numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# len() - get length
print(len(numbers))  # 9

# count() - count occurrences
print(numbers.count(1))  # 2
print(numbers.count(5))  # 2

# index() - find first occurrence
print(numbers.index(4))  # 2
print(numbers.index(5))  # 4

# sort() - sort in place
numbers.sort()
print(numbers)  # [1, 1, 2, 3, 4, 5, 5, 6, 9]

# sorted() - returns new sorted list
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 1, 2, 3, 4, 5, 5, 6, 9]
print(numbers)  # Original unchanged!

# reverse() - reverse in place
numbers.reverse()
print(numbers)  # [5, 6, 2, 9, 5, 1, 4, 1, 3]

# reversed() - returns iterator
for num in reversed(numbers):
    print(num)  # 3, 1, 4, 1, 5, 9, 2, 6, 5