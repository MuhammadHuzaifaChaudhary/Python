# function return 
# Functions returning multiple values (tuples)
def divide_with_remainder(a, b):
    """Return quotient and remainder"""
    return a // b, a % b

quotient, remainder = divide_with_remainder(17, 5)
print(f"17 / 5 = {quotient} remainder {remainder}")  # 17 / 5 = 3 remainder 2

def analyze_list(numbers):
    """Return multiple statistics about a list"""
    if not numbers:
        return 0, 0, None, None
    return sum(numbers), len(numbers), max(numbers), min(numbers)

data = [10, 20, 30, 40, 50]
total, count, max_val, min_val = analyze_list(data)
print(f"Total: {total}, Count: {count}, Max: {max_val}, Min: {min_val}")

