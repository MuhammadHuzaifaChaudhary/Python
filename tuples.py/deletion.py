# we cannot delete the portion of tuple because they are immutable 
# but we can delete the whole tuple using del keyword
t=(1,2,3,4,5)
del t
print(t)  # NameError: name 't' is not defined