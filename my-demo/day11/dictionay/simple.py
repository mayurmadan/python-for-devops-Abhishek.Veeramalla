name = {"name": "mayur" , "job": "devops", "age": 30}
print(name["age"])

name['age'] = 36  # Modifying a value
name['occupation'] = 'Engineer'  # Adding a new key-value pair
print(name)

#delete the element from dic
del(name["occupation"])
print(f"new value for dic is {name}")

#condition to check element 
if "ages" in name:
    print("age is present is dic")
else:
    print("no ages found in dic")

#here x is key and y is value for list element
    print(f"list print using for loop")
for x,y in name.items():    
    print(f"{x}: {y}")

