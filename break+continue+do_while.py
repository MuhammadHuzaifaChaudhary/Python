# do while loop do not exist in python
#  but we can simulate it using while loop
i = 0
while True:
    print(i)
    i += 1
    if i >= 5:
        break

# here you can see that the loop will always execute at least once, 
# even if the condition is false, because the condition 
# is checked after the first iteration.

# another example of do while 
while True:
    print("1. Option 1")
    print("2. Option 2")
    print("3. Exit")
    
    choice = int(input("Enter choice: "))
    
    # Process choice
    if choice == 1:
        print("Option 1 selected")
    elif choice == 2:
        print("Option 2 selected")
    elif choice == 3:
        break
    else:
        print("Invalid choice")

# continue statement in python
# it says skip that particular iteration and continue with the next iteration of the loop
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)  # This will only print odd numbers


# else with loop
# Case 1: No break - else RUNS
print("Case 1: No break")
for i in range(3):
    print(f"Loop: {i}")
else:
    print("ELSE runs!")  # This runs

# Output:
# Loop: 0
# Loop: 1
# Loop: 2
# ELSE runs!

print("\n" + "="*30 + "\n")

# Case 2: With break - else DOES NOT RUN
print("Case 2: With break")
for i in range(3):
    print(f"Loop: {i}")
    if i == 1:
        print("BREAK!")
        break
else:
    print("ELSE runs!")  # ❌ This does NOT run

# Output:
# Loop: 0
# Loop: 1
# BREAK!
# (ELSE block is skipped!)