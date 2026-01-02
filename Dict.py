# Dictionary : Mutable, Collection, unordered, key-value pairs

# Creating a dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print("Original Dictionary:", my_dict)

# Accessing values
print("Name:", my_dict['name'])
print("Age:", my_dict.get('age'))

# Adding a new key-value pair
my_dict['job'] = 'Engineer'
print("After Adding Job:", my_dict)

# Updating an existing value
my_dict['age'] = 31
print("After Updating Age:", my_dict)

# Removing a key-value pair
del my_dict['city']
print("After Deleting City:", my_dict)

# Iterating through keys and values

for key, value in my_dict.items():
    print(f"{key}: {value}")

# Checking if a key exists
if 'name' in my_dict:
    print("Name exists in the dictionary.")

# Getting all keys and values
keys = my_dict.keys()
values = my_dict.values()
print("Keys:", list(keys))
print("Values:", list(values))

# Clearing the dictionary
my_dict.clear()
print("After Clearing:", my_dict)
