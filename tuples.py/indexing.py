fruits = ("apple", "banana", "cherry", "date", "elderberry")

# Positive indexing
print(fruits[0])   # apple
print(fruits[2])   # cherry
print(fruits[4])   # elderberry

# Negative indexing
print(fruits[-1])  # elderberry
print(fruits[-2])  # date
print(fruits[-3])  # cherry

# Slicing works too!
print(fruits[1:3])   # ('banana', 'cherry')
print(fruits[:2])    # ('apple', 'banana')
print(fruits[2:])    # ('cherry', 'date', 'elderberry')
print(fruits[::-1])  # ('elderberry', 'date', 'cherry', 'banana', 'apple')
print(fruits[::2])  # ('apple', 'cherry', 'elderberry') 
# means it will start from index 0 and go till the end of the string and will take every second element.