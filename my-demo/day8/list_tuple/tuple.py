names = ("mayur", 129 , "pune", "groots")
print("output in list is\n",names)
print(type(names))

#tuple indexing
print("1st element of tuple is:",names[0])

#Tuple Length
print("lenght of tuple is", len(names))

##Common Tuple Operations
#Accessing Tuple Elements
print("lenght of 4th element is:", len(names[3]))

#Tuple Packing and Unpacking , assign identifier for element in tuble
name, location = (names[0], names[2])
print("name from tuple is:", name, "\nlocation from tuple is:", location)
print("name from tuple is:", names[0])

#Concatenating Tuples, can concatenate two or more tuples to create a new tuple.
new_name = ("sachin", 26, "akola")
print(names + new_name)
print(names + ("new value","19"))

#Checking for an Element
print("mayur" in names)


