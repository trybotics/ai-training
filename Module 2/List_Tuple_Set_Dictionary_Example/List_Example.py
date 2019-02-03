# Create a List:
thislist = ["apple", "banana", "cherry"]
print(thislist)

# You access the list items by referring to the index number:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
 print(x)

# Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
 print("Yes, 'apple' is in the fruits list")

# To determine how many items a list has, use the len() method:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# The remove() method removes the specified item:
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# The pop() method removes the specified index, (or the last item if index is not specified):
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# The del keyword removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# The del keyword can also delete the list completely:
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) #this will cause an error because "thislist" no longer exists.

# The clear() method empties the list:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
