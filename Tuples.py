# Tuple : Immutable, Collection, ordered, duplicate elements allowed
import sys
mytuple = (1, 2, 3, 4, 5, 1, 2)
print(mytuple[0])

mylist = list(mytuple)
print(mylist)

len_tuple = len(mytuple)
print(len_tuple)

# sclicing
print(mytuple[1:4])

# tuple unpacking

Tp1 = ("Max", 28, "Boston")

name, age, city = Tp1
print(name)
print(age)
print(city)

# IN bytes Tuple is more memory efficient than List


print(sys.getsizeof(mytuple))
print(sys.getsizeof(mylist))
