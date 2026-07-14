fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Positive indexing (0 to n-1)
print(fruits[0])   # apple
print(fruits[2])   # cherry
print(fruits[4])   # elderberry

# Negative indexing (from the end!)
print(fruits[-1])  # elderberry (last element)
print(fruits[-2])  # date (second last) its just the same length of the list -2 = 5-2 = 3 means 
# it will start from index 3 and go till the end of the string
print(fruits[-3])  # cherry

# Out of range error
# print(fruits[10])  # IndexError: list index out of range

# =================================================================================
# // C++ - Only positive indexing
# vector<string> fruits = {"apple", "banana", "cherry"};
# cout << fruits[0] << endl;   // apple
# cout << fruits[2] << endl;   // cherry
# // cout << fruits[-1];  // ❌ WRONG! Undefined behavior
# ==================================================================================

# Python - Both positive and negative!
fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # apple
print(fruits[-1])  # cherry  ← Python magic!

