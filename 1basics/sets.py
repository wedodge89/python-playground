# Set
my_set = {1, 2, 3, 4, 5, 5}
print(my_set)
# Note that items in a set cannot repeat; if user tries to add an item that already exists, that command is ignored.
my_set.add(100)
my_set.add(2)
print(my_set)

my_list = [1, 1, 2, 3, 4, 5, 5, 6]
print(set(my_list))

# Set Methods
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 5, 6, 7, 8, 9, 10}

print(set_1.difference(set_2))
print(set_2.difference(set_1))

set_1.discard(5)
print(set_1)

set_1.difference_update(set_2)
print(set_1)

print(set_1.intersection(set_2))
print(set_1 & set_2)

print(set_1.isdisjoint(set_2))

print(set_1.union(set_2))
print(set_1 | set_2)

print(set_1.issubset(set_2))
print(set_1.issuperset(set_2))