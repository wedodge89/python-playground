for i, char in enumerate("Hello"):
    print(i, char)

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f"Index of {char} is {i}.")