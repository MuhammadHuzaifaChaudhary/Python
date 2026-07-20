# Lexicographic comparison
print((1, 2, 3) < (1, 2, 4))    # True
print((1, 2, 3) < (1, 3, 2))    # True
print((1, 2, 3) == (1, 2, 3))   # True
print((1, 2, 3) < (2, 1, 1))    # True (first element 1 < 2)

# Useful for sorting
points = [(5, 2), (1, 3), (4, 1), (2, 5)]
points.sort()
print(points)  # [(1, 3), (2, 5), (4, 1), (5, 2)]