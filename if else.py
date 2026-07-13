# # No parentheses around condition (though you can use them)
# No braces {} - uses indentation (usually 4 spaces)
# elif instead of else if
# Colon : after condition
# No semicolons ; at line ends
score = 85
if score >= 90:
    print("A")
elif score >= 80:  # Note: 'elif' not 'else if'
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

# if (age >= 18 && hasLicense) {
#     cout << "Can drive";
# }

# in python 

# if age >= 18 and has_license:         # 'and' not '&&'
#     print("Can drive")

# identation is very important in python because 
# it is used to define the block of code.

if 'a' in ['a', 'b', 'c']:
    print("Found!")  # No direct C++ equivalent without loops

# C++ would need: if (x > 0 && x < 10)
# python syntax 

x=9;
if 0 < x < 10:  # Python allows this!
    print("x is between 0 and 10")

# ternary operator in c++
# int max = (a > b) ? a : b;

a=5;
b=10;
max_val = a if a > b else b  # Note the order!
# Syntax: value_if_true if condition else value_if_false

# if x > 5:
# print("Hello")  # ❌ IndentationError
#     print("World")  # ❌ Mixed indentation