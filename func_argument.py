

def describe_pet(name, animal_type):
    print(f"I have a {animal_type} named {name}")

# Call with positional arguments
describe_pet("Max", "dog")    # I have a dog named Max
describe_pet("Whiskers", "cat")  # I have a cat named Whiskers




# call with default arguments
# Default parameters (C++ equivalent but more flexible)
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")           # Hello, Alice! (uses default)
greet("Bob", "Hi")       # Hi, Bob!
greet("Charlie", "Good morning")  # Good morning, Charlie!

# Multiple default parameters
def create_user(name, age=18, city="Unknown"):
    print(f"User: {name}, Age: {age}, City: {city}")

create_user("John")                    # User: John, Age: 18, City: Unknown
create_user("Sarah", 25)               # User: Sarah, Age: 25, City: Unknown
create_user("Mike", 30, "New York")    # User: Mike, Age: 30, City: New York



# Keyword arguments make code more readable!
def describe_pet(name, animal_type, age):
    print(f"{name} is a {animal_type} and is {age} years old")

# Positional
describe_pet("Max", "dog", 3)

# Keyword (order doesn't matter!)
describe_pet(animal_type="cat", name="Whiskers", age=5)
describe_pet(name="Buddy", age=2, animal_type="bird")

# Mix positional and keyword (positional must come first!)
describe_pet("Max", animal_type="dog", age=3)  # ✅ Correct
# describe_pet(name="Max", "dog", age=3)  # ❌ SyntaxError!

