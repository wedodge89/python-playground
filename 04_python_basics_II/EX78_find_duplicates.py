# Exercise: Check for duplicates in list:
some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]
checker = []
duplicates = []

for item in some_list:
    if item not in checker:
        checker.append(item)
    else:
        duplicates.append(item)

print(duplicates)

# andre's solution
duplicates = []
for value in some_list:
    if some_list.count(value) >1:
       if value not in duplicates:
            duplicates.append(value)

print(duplicates)