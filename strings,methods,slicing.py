#string slicing is used to get a part of string from the whole string
# we can do it by using indexing and slicing
# first write variable name then use sqaure brackets 
# after it write the index [start:end]
b="huzaifa!!!!!!"
print(b[0:3]) 
# it will print only the first 3 characters
#  of the string i.e. huz
# 0 se start hoga aur 3 tak jaayega but 3 ko include nahi karega
print(b[0:]) 
# its work is same as b[0:len(b)] i.e. it will print the whole string
print(b[:3])
# it will print the first 3 characters of the string i.e. huz
# means if we dont write something at start means its start from 0 
# and if we dont write something at end means it will go till the 
# end of the string

# negatuve slicing 
print(b[-3:])
# python means it will automatically do len(b)-3 = 4 means it will
#  start from index 4 and go till the end of the string


# here are few methods of string
# string are immutable means we cannot change the string once it is created
# its not conerting them but it will create a new string and assign it to the variable
print(b.upper())  # converts string to uppercase
print(b.lower())  # converts string to lowercase
print(b.capitalize())  # converts first character to uppercase and rest to lowercase
print(b.title())  # converts first character of each word to uppercase
print(b.swapcase())  # swaps the case of each character
# means if it is lower case then it will convert it to uppercase and vice versa
print(b.strip())  # removes whitespace from both ends of the string
print(b.lstrip())  # removes whitespace from left end of the string
print(b.rstrip("!"))  # removes whitespace or the mark you type
# in bracket # from right end of the string 
print(b.replace("!", "?"))  # replaces all occurrences of "!" with "?"

countstr=b.count("a")
print(countstr)  # counts the number of occurrences of "a" in the string
print(b.find("a"))  # returns the index of the first occurrence of "a" in the string
print(b.index("a"))  # returns the index of the first occurrence of "a" in the string
print(b.startswith("h"))  # returns True if the string starts with "h"
print(b.endswith("!", 4, 7))  # returns True if the string ends with "!" between indices 4 and 7
# yani 4 index se 7 tak select hay or usme agr ! par end ho rahi hay to true 
print(b.endswith("!"))  # returns True if the string ends with "!"
print(b.isalpha())  # returns True if the string contains only alphabetic characters
print(b.isdigit())  # returns True if the string contains only digits
print("alphanumeric")
print(b.isalnum())  # returns True if the string contains only alphanumeric characters
# alphanumeric means it contains both alphabets and numbers
# if there are alphabets then it willl give false 
print(b.islower())  # returns True if the string contains only lowercase characters
print(b.isupper())  # returns True if the string contains only uppercase characters
print(b.isspace())  # returns True if the string contains only whitespace characters
a="huz\n"
print(a)
print(a.isprintable()) 
 # returns True if the string contains only printable characters
#  because \n is not printable character so it will return false
c=("how are you")
print(c.istitle())  
# returns True if the string have uppercase character
#  at the start of each word
print(c.title())  # converts first character of each word to uppercase