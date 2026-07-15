fruits = ("apple", "banana", "cherry")

# ❌ These will cause errors!
# fruits[0] = "orange"     # TypeError: 'tuple' object does not support item assignment
# fruits.append("date")    # AttributeError: 'tuple' object has no attribute 'append'
# fruits.remove("apple")   # AttributeError: 'tuple' object has no attribute 'remove'
# fruits[1:3] = ["x", "y"] # TypeError: 'tuple' object does not support item assignment

# But you CAN create new tuples from existing ones
new_fruits = fruits + ("date", "elderberry")
print(new_fruits)  # ('apple', 'banana', 'cherry', 'date', 'elderberry')

# OR
new_fruits = (*fruits, "date", "elderberry")
print(new_fruits)  # ('apple', 'banana', 'cherry', 'date', 'elderberry')
# if we will not play asterisk then output will be (('apple', 'banana', 'cherry'), 'date', 'elderberry')
#  which is not correct because it will consider the last two elements as a tuple and will add it to the original tuple.

# ===================================================
# mutable thing 
# ====================================================

# Tuple containing a list
mixed = (1, 2, [3, 4, 5])

# You CAN modify the list inside the tuple
mixed[2][0] = 99
print(mixed)  # (1, 2, [99, 4, 5])  ← List changed!

# But you CANNOT replace the list itself
# mixed[2] = [6, 7, 8]  # ❌ TypeError!  .

# Why? The tuple holds a reference to the list object
# You can change what's inside the list, but not the reference itself