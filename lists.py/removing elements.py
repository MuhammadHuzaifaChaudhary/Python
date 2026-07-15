fruits = ["apple", "banana", "cherry", "date", "banana"]

# remove() - remove first occurrence
fruits.remove("banana")  # Removes first 'banana'
print(fruits)  # ['apple', 'cherry', 'date', 'banana']

# pop() - remove and return last element
last = fruits.pop()
print(last)    # banana
print(fruits)  # ['apple', 'cherry', 'date']

# pop(index) - remove at specific index
removed = fruits.pop(1)
print(removed) # cherry
print(fruits)  # ['apple', 'date']

# del - delete by index or slice
del fruits[0]
print(fruits)  # ['date']

# clear() - remove all elements
fruits.clear()
print(fruits)  # []

# =====================================================================
# C++ equivalent
# =====================================================================

# # vector<string> fruits = {"apple", "banana", "cherry"};
# // Remove by value (needs find)
# auto it = find(fruits.begin(), fruits.end(), "banana");
# if (it != fruits.end()) fruits.erase(it);
# // pop_back() - remove last
# fruits.pop_back();
# // erase - remove at position
# fruits.erase(fruits.begin() + 1);

# =====================================================================