# Use Tuples When:
# Data should never change (constants)

# Dictionary keys (tuples can be keys, lists cannot)

# Function returning multiple values

# Performance matters (tuples are faster and use less memory)

# Data represents fixed structure (like coordinates)


# ==============================
# example
# ===============================

# 1. Constants
DAYS_OF_WEEK = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

# 2. Dictionary keys (lists can't be keys!)
coordinates = {
    (0, 0): "Origin",
    (1, 0): "Right",
    (0, 1): "Up",
    (1, 1): "Diagonal"
}
print(coordinates[(1, 0)])  # Right

# 3. Returning multiple values
def get_user_info():
    return "Alice", 25, "alice@email.com"

name, age, email = get_user_info()

# 4. Fixed data structures
RGB_RED = (255, 0, 0)
RGB_GREEN = (0, 255, 0)
RGB_BLUE = (0, 0, 255)