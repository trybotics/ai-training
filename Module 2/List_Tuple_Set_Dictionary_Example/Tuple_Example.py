# Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Return the item in position 1:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# You cannot change values in a tuple:
thistuple = ("apple", "banana", "cherry")
thistuple[1] = "blackcurrant"
# The values will remain the same:
print(thistuple)

# Iterate through the items and print the values:
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# Check if "apple" is present in the tuple:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

# Print the number of items in the tuple:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# You cannot add items to a tuple:
thistuple = ("apple", "banana", "cherry")
thistuple[3] = "orange" # This will raise an error
print(thistuple)

# The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

# Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)