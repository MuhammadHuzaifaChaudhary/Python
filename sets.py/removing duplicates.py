# The problem: remove duplicates but keep original order
items = [3, 1, 2, 3, 4, 1, 5, 2, 3]

# Method 1: Using list comprehension with set (doesn't preserve order)
unique_set = set(items)
print(list(unique_set))  # [1, 2, 3, 4, 5] (order not preserved)

# Method 2: Using a set to track seen items (preserves order)
seen = set()
unique_ordered = []
for item in items:
    if item not in seen:
        seen.add(item)
        unique_ordered.append(item)
print(unique_ordered)  # [3, 1, 2, 4, 5] (order preserved)

# Method 3: Using dict.fromkeys() (preserves order, Python 3.7+)
unique_ordered = list(dict.fromkeys(items))
print(unique_ordered)  # [3, 1, 2, 4, 5]