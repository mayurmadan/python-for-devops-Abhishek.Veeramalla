names = ["mayur", 129 , "pune", "groots"]
print("output in list is\n",names)
print(type(names))

#List Indexing
#List elements are indexed, starting from 0 for the first element. You can access elements by their index.
print(names[0],names[1])

#List Length
print(len(names), names[1])

##List Manipulation and Common List Operations
#Appending to a List , we can add only a single element
names.append("mss-cet")
print("new list is:",names)

#Removing from a List
names.remove("pune")
print("new list after delete is:",names)

#Slicing a List:- allows you to create a new list from a subset of the original list.
new_list = names[0:2] #read upto 3rd elment from LHS but not include 3rd element
print("new list is:", new_list)

#Concatenating Lists
new_concated_list = names + [12,"mayur"]
print("new concated string is:", new_concated_list)
print(new_concated_list[0] + "," + names[3] )

#Sorting a List [error comes]
x = [1288,197937,803]
x.sort()
print(x)

