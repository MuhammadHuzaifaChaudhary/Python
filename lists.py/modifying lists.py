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

# ==========================================================
# more examples 
# ==========================================================
numbers = [1, 2, 3, 4, 5]

# Change single element
numbers[2] = 99
print(numbers)  # [1, 2, 99, 4, 5]

# Change multiple elements with slicing
numbers[1:4] = [10, 20, 30]
print(numbers)  # [1, 10, 20, 30, 5]

# Replace with different length
numbers[1:3] = [100, 200, 300, 400]
print(numbers)  # [1, 100, 200, 300, 400, 30, 5]

# Delete with slice assignment
numbers[1:4] = []  # Remove elements
print(numbers)  # [1, 400, 30, 5]

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