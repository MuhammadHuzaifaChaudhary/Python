# ❌ WRONG - This is NOT a tuple!
not_tuple = (5)
print(type(not_tuple))  # <class 'int'>

# ✅ CORRECT - Need a comma!
is_tuple = (5,)
print(type(is_tuple))  # <class 'tuple'>

# Also works without parentheses
another_tuple = 5,
print(type(another_tuple))  # <class 'tuple'>

# ==================================================================

fruits = ("apple", "banana", "cherry")

# ❌ These all fail!
# fruits[0] = "orange"  # TypeError
# fruits.append("date")  # AttributeError
# fruits.remove("apple") # AttributeError
# del fruits[1]          # TypeError

# ✅ Instead, create a new tuple
new_fruits = ("orange",) + fruits[1:]
print(new_fruits)  # ('orange', 'banana', 'cherry')



