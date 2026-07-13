# int i = 0;
# while (i < 5) {
#     cout << i << endl;
#     i++;
# } its in c++

# in python 
i = 0
while i < 5:
    print(i)
    i += 1  # No i++ in Python!



    # Basic countdown
count = 5
while count > 0:
    print(count)
    count -= 1
print("Blast off!")

# User input until valid
user_input = ""
while user_input != "quit":
    user_input = input("Enter 'quit' to exit: ")
    print("You entered: ,user_input")

#  f string is also used to format the string in python and 
# it is more efficient than + operator to concatenate the string and variable.
# Infinite loop with break
while True:
    command = input("Enter command: ")
    if command == "exit":
        break
    print(f"Executing: {command}")

# Game loop
health = 100
while health > 0:
    damage = int(input("Enter damage: "))
    health -= damage
    print(f"Health: {health}")
print("Game Over!")