# Define the Dictionary
myFriends = {"Sandy": 25, "John": 20, "Jane": 22}

# Accessing components
print(myFriends.items())   # View all pairs
print(myFriends.keys())    # View all names
print(myFriends.values())  # View all ages
print(myFriends["Sandy"])  # Get Sandy's age -> 25

# Updating values
myFriends["Sandy"] = 30    # Change age to 30
print(myFriends.items())

myFriends.update({"Sandy": 40}) # Update method
print(myFriends.items())

# Removing items
myFriends.pop("Sandy")     # Removes Sandy specifically
print(myFriends.items())

myFriends.popitem()        # Removes the last inserted item
print(myFriends.items())

del myFriends["John"]      # Another way to delete a specific key
print(myFriends.items())