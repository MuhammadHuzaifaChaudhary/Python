fruits = {"apple", "banana", "cherry"}

# add() - add single element
fruits.add("date")
print(fruits)  # {'apple', 'banana', 'cherry', 'date'}

# Adding duplicate doesn't change anything
fruits.add("apple")  # No effect!
print(fruits)  # {'apple', 'banana', 'cherry', 'date'}

# update() - add multiple elements
fruits.update(["elderberry", "fig", "grape"])
print(fruits)  # {'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape'}

# remove() - remove element (raises error if not found)
fruits.remove("banana")
print(fruits)  # {'apple', 'cherry', 'date', 'elderberry', 'fig', 'grape'}

# discard() - remove element (no error if not found)
fruits.discard("mango")  # No error!

# pop() - remove and return an arbitrary element
random_fruit = fruits.pop()
print(f"Removed: {random_fruit}")
print(fruits)

# clear() - remove all elements
fruits.clear()
print(fruits)  # set()

# ===================================================================================
# c++
# ===================================================================================
# set<string> fruits = {"apple", "banana", "cherry"};

# // Insert
# fruits.insert("date");
# fruits.insert("apple");  // No effect (already exists)

# // Erase
# fruits.erase("banana");

# // Find and remove
# auto it = fruits.find("mango");
# if (it != fruits.end()) {
#     fruits.erase(it);
# }

# // Clear
# fruits.clear();
