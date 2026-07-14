fruits = ["apple", "banana"]

# append() - add at end
fruits.append("cherry")
print(fruits)  # ['apple', 'banana', 'cherry']

# insert() - add at specific position
fruits.insert(1, "blueberry")
print(fruits)  # ['apple', 'blueberry', 'banana', 'cherry']

# extend() - add multiple elements
fruits.extend(["date", "elderberry"])
print(fruits)  # ['apple', 'blueberry', 'banana', 'cherry', 'date', 'elderberry']

# + operator - concatenate
more_fruits = ["fig", "grape"]
all_fruits = fruits + more_fruits
print(all_fruits)  # ['apple', 'blueberry', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']

fruits.reverse()
print(fruits)  # ['elderberry', 'date', 'cherry', 'banana', 'blueberry', 'apple']

nums=[1,2,7,5,9,3,10]
nums.sort()
print(nums) # [1, 2, 3, 5, 7, 9, 10]

# ====================================================================

# C++ equivalent 

# ====================================================================

# #include <vector>
# vector<string> fruits = {"apple", "banana"};

# // push_back() - add at end
# fruits.push_back("cherry");

# // insert() - add at specific position
# fruits.insert(fruits.begin() + 1, "blueberry");

# // No direct extend equivalent

# =========================================================================