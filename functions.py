# #include <iostream>
# using namespace std;

# // Function declaration (prototype)
# int add(int a, int b);

# // Function definition
# int add(int a, int b) {
#     return a + b;
# }

# int main() {
#     int result = add(5, 3);
#     cout << result << endl;
#     return 0;
# }


# Function definition (no prototype needed!)
def add(a, b):
    return a + b

# Function call
result = add(5, 3)
print(result)

# No return type needed!
def greet(name):
    print(f"Hello, {name}!")

# Call the function
greet("Alice")  # Hello, Alice!

# Function with return value
def add(a, b):
    return a + b

result = add(10, 5)
print(result)  # 15

# Function with multiple returns
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

minimum, maximum, average = get_stats([1, 2, 3, 4, 5])
print(f"Min: {minimum}, Max: {maximum}, Avg: {average:.2f}")


a=10
b=9
if(a>b):
    pass 
# this pass will say python to do nothing and 
# continue with the rest of the code.