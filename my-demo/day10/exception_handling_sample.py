import sys
x = int(sys.argv[1])
y = int(sys.argv[2])

#divide 
try:
    z = x/y
except ZeroDivisionError:
    print("value not able to divide by zero")
print(z)

