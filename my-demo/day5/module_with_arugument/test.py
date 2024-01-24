import test_module

#this module is used for passing command line argument in python, default type for arugument is string
import sys

#user pass arugument in form of 
# script.py x add/sub/mul/div y
x = int(sys.argv[1])
operation = sys.argv[2]
y = int(sys.argv[3])

if operation == "add":
    addition = test_module.add(x,y)
    print("addition is:",addition)
elif operation == "mul":
    print("multiplication is:",test_module.mul(x,y))
elif operation == "div":
    print("dividation is:",test_module.div(x,y))
elif operation == "sub":
    print("substraction is:", test_module.sub(x,y))
    



