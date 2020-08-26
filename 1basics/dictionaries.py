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