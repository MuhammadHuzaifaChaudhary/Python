# Global variable
global_var = 10

def my_function():
    # Local variable
    local_var = 5
    print(f"Local: {local_var}")
    print(f"Global (read): {global_var}")

my_function()
# print(local_var)  # ❌ NameError: local_var not defined

# Modifying global variable
counter = 0

def increment():
    global counter  # Need global keyword to modify
    counter += 1
    print(f"Counter: {counter}")

increment()  # Counter: 1
increment()  # Counter: 2
print(counter)  # 2