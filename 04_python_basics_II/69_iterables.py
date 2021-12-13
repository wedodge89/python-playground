# an iterable is any object that can be iterated (looped) over
# list, dictionary, tuple, set, string

user = {
    "name": "Elliott",
    "age": "31",
    "can_swim": True
}

for item in user.items():
    print(item)

for item in user.keys():
    print(item)

for item in user.values():
    print(item)

for k, v in user.items():
    print(f"{k}: {v}")