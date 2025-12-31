# Data Types in Python
student_count = 1000  # integer
rating = 4.4  # float
is_published = True  # boolean
course_name = "Python Programming"  # string

print(student_count)

# Sring Manipulation
course_name = "Python Programming"
print(len(course_name))  # Length of the string
print(course_name[0])  # First character
print(course_name[-1])  # Last character
print(course_name[0::2])  # Sclicing with step
print(course_name[0:3])  # Slicing from index 0 to 2
print(course_name.upper())  # Convert to uppercase
print(course_name.lower())  # Convert to lowercase

# Escape Sequences
# /""
# /''
# /n
# //

first_name = "john"
last_name = "doe"
full_name = f"{first_name} {last_name}"
print(full_name)  # Formatted string and concatenation

print(full_name.upper())  # Uppercase full name
print(full_name.title())  # Title case full name
print(full_name.strip())  # Remove leading/trailing whitespace
print(full_name.replace("john", "jane"))  # Replace substring
print(full_name.find("joe"))  # Find substring index

# complex data types
numbers = 1 + 2j  # complex number
print(numbers)

# Operations
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

# Type Conversion
x = "100"
int(x)  # Convert to integer
float(x)  # Convert to float
str(x)  # Convert to string
bool(x)  # Convert to boolean

# Conditional Statements
temperature = 35
if temperature > 30:
    print("It's a warm day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It's a nice day")
else:
    print("It's cold day")
print("Enjoy your day")

# Ternary Operator
age = 20
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)


# For Loop

for i in range(5):
    print("send a message", i+1)

sucessful = False
for i in range(5):
    print("Attempt", i+1)
    if sucessful:
        print("Successful")
        break
else:
    print("Attempted 5 times and failed")

# Nested Loops
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")

# While Loop

number = 100
while number >= 1:
    print(number)
    number //= 2


def greet_user(name):
    print(f"{name},Welcome aboard!")


greet_user("John")
