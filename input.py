#we can take input from user using input() function
name = input("Enter your name: ")
print('Hello, ' + name + '!')

#we can also do 
print("enter your age: ")
age=input()
print("You are " + age + " years old.")
#as age is string here suppose we take it in 
# int(input(enetr your age:)) then we we will use commas instead 
# of + to print the age because we cannot concatenate
#  string and integer.

# if you want to use + then you have to do str(age) means 
# again convert it into string to print 
# because + can only concatenate string and string not 
# string and integer.

# here + is used to concatenate the string and variable.

# python input is always a string, 
# so if we want to take integer input we have to convert it 
# into integer using int() function.
gpa = int(input("Enter your gpa: "))
cgpa = int(input("Enter your cgpa: "))
print(gpa+cgpa)
# we can also do print(int(gpa)+int(cgpa)) 
# if gpa and cgpa are string type but it is not a good practice 
