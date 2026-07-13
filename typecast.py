# typecasting in python 
# if we do a="1" and b="2" then a+b will just do 
# concatenation of a and b i.e. 12
#  but if we want to add them then we can do it by typecasting
a="1"
b="2"
m=int(a)+int(b) # here we are typecasting a and b to int
print(m) # now it will print 3 instead of 12
#python does not have character data type 
# if we do character addition in c++ then it will 
# give us the sum of ascii values of those characters
# but in order to get ascii value sum in python 
# we can do it by using ord() function
y=ord('a')+ord('b') # here we are typecasting a and b to int
print(y) 
# now it will print the sum of ascii values of 'a' and 'b'