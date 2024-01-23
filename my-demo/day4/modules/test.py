import test_module

x = int(input("enter the value for x:"))
y = int(input("enter the value for y:"))

print("value after calling add modules",test_module.add(x,y))
print("value after calling mul_by_2 modules",test_module.mul_by_2(x))
print("value after calling sub modules:",test_module.sub(x,y))
