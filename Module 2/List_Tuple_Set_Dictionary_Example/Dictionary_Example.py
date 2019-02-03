# Create and print a dictionary:
thisdict =	{
  "brand": "Mi",
  "model": "Note 7",
  "year": 2019
}
print(thisdict)

# Get the value of the "model" key:
thisdict =	{
  "brand": "Mi",
  "model": "Note 7",
  "year": 2019
}
x = thisdict["model"]
print(x)

# There is also a method called get() that will give you the same result:
thisdict =	{
  "brand": "Mi",
  "model": "Note 7",
  "year": 2019
}
x = thisdict.get("model")
print(x)

# You can change the value of a specific item by referring to its key name: Change the "year" to 2018:
thisdict =	{
  "brand": "Mi",
  "model": "Note 7",
  "year": 2019
}
thisdict["year"] = 2018
print(thisdict)

# Print all key names in the dictionary, one by one:
thisdict =	{
  "brand": "Mi",
  "model": "Note 7",
  "year": 2019
}
for x in thisdict:
  print(x)

# Print all values in the dictionary, one by one:
thisdict =	{
  "brand": "Mi",
  "model": "Note 7",
  "year": 2019
}
for x in thisdict:
  print(thisdict[x])

# You can also use the values() function to return values of a dictionary:
thisdict =	{
  "brand": "Mi",
  "model": "Note 7",
  "year": 2019
}
for x in thisdict.values():
  print(x)

# Loop through both keys and values, by using the items() function:
thisdict =	{
  "brand": "Mi",
  "model": "Note 7",
  "year": 2019
}
for x, y in thisdict.items():
  print(x, y)

# Check if "model" is present in the dictionary:
thisdict =	{
  "brand": "Mi",
  "model": "Note 7",
  "year": 2019
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Print the number of items in the dictionary:
thisdict =	{
  "brand": "Mi",
  "model": "Note 7",
  "year": 2019
}
print(len(thisdict))

# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
thisdict =	{
  "brand": "Mi",
  "model": "Note 7",
  "year": 2019
}
thisdict["color"] = "red"
print(thisdict)

# The pop() method removes the item with the specified key name:
thisdict =	{
  "brand": "Mi",
  "model": "Note 7",
  "year": 2019
}
thisdict.pop("model")
print(thisdict)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict =	{
  "brand": "Mi",
  "model": "Note 7",
  "year": 2019
}
thisdict.popitem()
print(thisdict)

# The del keyword removes the item with the specified key name:
thisdict =	{
  "brand": "Mi",
  "model": "Note 7",
  "year": 2019
}
del thisdict["model"]
print(thisdict)

# The del keyword can also delete the dictionary completely:
thisdict =	{
  "brand": "Mi",
  "model": "Note 7",
  "year": 2019
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.

# The clear() keyword empties the dictionary:
thisdict =	{
  "brand": "Mi",
  "model": "Note 7",
  "year": 2019
}
thisdict.clear()
print(thisdict)

# It is also possible to use the dict() constructor to make a dictionary:
thisdict =	dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)