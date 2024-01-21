# Creating a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing values
print("my Name is:", my_dict['name'])
print("my Age is:", my_dict['age'])

# Adding a new key-value pair
my_dict['email'] = 'john@example.com'
print("Updated dictionary:", my_dict)

# Iterating through keys and values
#here is used as a treat as key and b treat as value  
for a, b in my_dict.items():
    print(f"{a}: {b}")
