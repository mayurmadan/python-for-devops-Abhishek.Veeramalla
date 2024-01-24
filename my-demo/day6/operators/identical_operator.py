#dentity operators in Python are used to compare the memory locations of two objects to determine if they are the same object or not. The two identity operators are "is" and "is not."
a = 12
b =17

#is: Returns True if both operands refer to the same object.
print(a is b)

#is not: Returns True if both operands refer to different objects.
print(a is not b)

##example2
x = [12,15,18]
y = (12,15,18)

print(x is y) # will return false as both data type is diff list & tuple
print(x is not y)

#using membership operator here
print(25 in x)
print(25 not in x)
