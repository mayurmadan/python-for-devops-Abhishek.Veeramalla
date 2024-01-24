#include the basic assignment operator (=) and various compound assignment operators that perform an operation on the variable while assigning a value.
a= 100

#Basic Assignment (=): Assigns a value to a variable.

#Addition Assignment (+=): Adds the right operand to the left operand and assigns the result to the left operand.
a += 10 #its like a = a+ 10
print("updated value of a is:",(a)) #will give value of a by adding 10 in it.

#Subtraction Assignment (-=)
a -= 20 
print(a) #here it will use last value of a , i.e 110 from last  Addition Assignment (+=)

#Multiplication Assignment (*=)
b = 10
a *= b
print (a)

#Division Assignment (/=)
a /= 12
print(a)

#Floor Division Assignment (//=)
a //= 5
print(a)

#Modulus Assignment (%=)[baki]
a %= 4
print(a)

#Exponentiation Assignment (=):** 
a **= 2
print(a)
