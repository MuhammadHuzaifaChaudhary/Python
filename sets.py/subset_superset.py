set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 4}
set3 = {1, 2, 3, 4, 5, 6}

# issubset() - check if all elements are in another set
print(set2.issubset(set1))  # True (set2 ⊆ set1)
print(set1.issubset(set2))  # False

# issuperset() - check if contains all elements of another set
print(set1.issuperset(set2))  # True (set1 ⊇ set2)
print(set2.issuperset(set1))  # False

# isdisjoint() - check if no common elements
set4 = {6, 7, 8}
print(set1.isdisjoint(set4))  # True (no common elements)
print(set1.isdisjoint(set2))  # False (share 2, 3, 4)

# Subset with <= and < (strict subset)
print(set2 <= set1)  # True (subset)
print(set2 < set1)   # True (proper subset)
print(set1 < set1)   # False (not proper subset)

