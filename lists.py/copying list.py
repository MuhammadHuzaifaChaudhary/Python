original = [1, 2, 3, 4, 5]

# Method 1: Slice copy (recommended)
copy1 = original[:]

# Method 2: list() constructor
copy2 = list(original)

# Method 3: copy() method
copy3 = original.copy()

# BAD WAY - This doesn't copy!
bad_copy = original  # Both refer to same list
bad_copy[0] = 99
print(original)  # [99, 2, 3, 4, 5] ← Original changed!

# Modifying copy doesn't affect original
copy1[0] = 999
print(original)  # [99, 2, 3, 4, 5] (unchanged)