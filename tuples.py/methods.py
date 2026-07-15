fruits = ("apple", "banana", "cherry", "banana")

# count() - count occurrences
print(fruits.count("banana"))  # 2
print(fruits.count("apple"))   # 1
print(fruits.count("grape"))   # 0

# index() - find first occurrence
print(fruits.index("cherry"))  # 2
print(fruits.index("banana"))  # 1 (first occurrence)

# len() - length
print(len(fruits))  # 4

# in operator - membership
print("banana" in fruits)   # True
print("grape" in fruits)    # False

# Not many methods because tuples are immutable!