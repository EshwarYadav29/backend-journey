# List : Mutable , Collection , ordered , duplicate elements allowed
myList1 = ["banana", "apple", "cherry"]

print(myList1)

myList2 = [True, False, 10, 15.5, "Hello", "Hello"]
print(myList2),

item = myList1[0]
print(item)

# loop Iterarion
for i in myList1:
    print(i)

if ("apple" in myList1):
    print("Yes , apple is present in the list")
else:
    print("No , apple is not present in the list")

lenOfList = len(myList1)
print("Length of the list is : ", lenOfList)

myList1.append("orange")
print(myList1)

myList1.insert(1, "kiwi")
print(myList1)

myList1.remove("banana")
print(myList1)

myList1.sort()
print(myList1)

myList1.reverse()
print(myList1)
