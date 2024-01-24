#Logical operators in Python are used to manipulate and combine Boolean values. These operators allow you to perform logical operations such as AND, OR, and NOT.
a = "abc"
b = "abc"

result = a == b
x = (result)  #will return true as both are same

y = (a != b) # will return false as both are diff

#AND (and): Returns True if both operands are True.
print(x and y) #return false as one is false

#OR (or): Returns True if at least one of the operands is True.
print(x or y) #return true as one is true

#NOT (not): Returns the opposite Boolean value of the operand.
print(not x) # wil opposite the boolen value for x to false from true

