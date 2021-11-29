user = {
    "basket": [1, 2, 3],
    "greet": "hello",
    "age": 20
}

# find string in dict
print("basket" in user)
print("size" in user)
# find the string in keys of dict
print("greet" in user.keys())
print("hello" in user.keys())
# find the string in values of dict
print("greet" in user.values())
print("hello" in user.values())
# print keys and values together as tuples
print(user.items())
# create a copy of the dict
user2 = user.copy()
# delete all keys and values from dict
user.clear()
print(user)
print(user2)
# remove and return the named item from dict
print(user2.pop("age"))
print(user2)
# change value for a given key
user2.update({"age": 31})
user2.update({"status": "okay"})
print(user2)