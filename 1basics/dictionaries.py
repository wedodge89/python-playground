# Dictionary
dictionary = {
    "a": 1,
    "b": 2,
    "x": 3,
    "y": [1, 2, 3]
}

print(dictionary["b"])
print(dictionary["y"][1])

# Dictionary Keys
# Key must be unique and immutable
weird_dictionary = {
    123: [1, 2, 3],
    True: "hello",
    True: "goodbye"
}
print(weird_dictionary[123])
print(weird_dictionary[True])

# Dictionary Methods
user = {
    "basket": ["item1", "item2", "item3"],
    "greeting": "hello"
}

# .get - Searches for a specific key without risking breaking the program
# Second param fills in if no value is found for that key
print(user.get("age"))
print(user.get("age", 55))
# dict (built in method) - can be used to create a new dictionary with the specified key(s) and value(s)
user2 = dict(name = "Frank")
print(user2)
# in - returns True or False depending on whether that key exists in a dictionary.
print("basket" in user)
print("basket" in user.keys())
print("basket" in user.values())
# clear - empties the named dictionary
user2.clear()
print(user2)
# copy - copies the second named dict to the first
user2 = user.copy()
print(user2)
# pop - removes and returns the value for the named key
print(user.pop("basket"))
print(user)
# popitem - removes a randomly selected item
# update - changes or adds the kv-pair named
print(user.update({"age": 55}))
print(user)