dictionary = {
    123: [1, 2, 3],
    True: "hello",
    "is_magic": True
}
print(dictionary[123])
print(dictionary[True])
print(dictionary["is_magic"])

# in short, dict keys must be immutable
# if a key is repeated, the later instance will overwrite the previous