#we can take input from user using input() function
name = input("Enter your name: ")
print('Hello, ' + name + '!')

#we can also do 
print("enter your age: ")
age=input()
print("You are " + age + " years old.")
# here + is used to concatenate the string and variable.
# python input is always a string, 
# so if we want to take integer input we have to convert it 
# into integer using int() function.
gpa = int(input("Enter your gpa: "))
cgpa = int(input("Enter your cgpa: "))
print(gpa+cgpa)