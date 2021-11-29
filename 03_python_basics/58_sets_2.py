my_set = {1, 2, 3, 4, 5, 6, 7, 8}
your_set = {4, 5, 6, 7, 8, 9, 10}

# shows items unique to first named set
print(my_set.difference(your_set))
print(your_set.difference(my_set))

# remove the item named
my_set.discard(5)
print(my_set)

# remove the common items
your_set.difference_update(my_set)
print(your_set)

# returns common items
print(my_set.intersection(your_set))

# returns True is there are any items in common
print(my_set.isdisjoint(your_set))

# returns True if first set is contained within second
print(my_set.issubset(your_set))

# returns True if first set contains all of second
print(my_set.issuperset(your_set))

# returns two sets combined, sans duplicates
print(my_set.union(your_set))