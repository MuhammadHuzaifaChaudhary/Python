# as in c++ we directly do 
# int add(int a, int b) { return a + b; }
# double add(double a, double b) { return a + b; }
# int add(int a, int b, int c) { return a + b + c; }

# but in python we can not do this as python does not support function overloading.
#  but here are alternatives 

# by using default parameters
def add(a, b, c=0):
    return a + b + c

print(add(5, 3))       # 8
print(add(5, 3, 2))    # 10


# second way is type checking
# using keyword isinstance(variable,typename)
def add(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, float) and isinstance(b, float):
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        return a + " " + b
    else:
        raise TypeError("Unsupported types")

print(add(5, 3))        # 8
print(add(5.5, 3.2))    # 8.7
print(add("Hello", "World"))  # Hello World




# or by using singled ispatch function

from functools import singledispatch

@singledispatch
def process(value):
    print(f"Default: {value}")

@process.register(int)
def _(value):
    print(f"Integer: {value}")

@process.register(str)
def _(value):
    print(f"String: {value}")

@process.register(list)
def _(value):
    print(f"List with {len(value)} items")

process(42)        # Integer: 42
process("hello")   # String: hello
process([1, 2, 3]) # List with 3 items
process(3.14)      # Default: 3.14


