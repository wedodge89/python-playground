my_tuple = (1, 2, 3, 4, 5, 5)
new_tuple = my_tuple[:2]
(x, y, z, *other) = (1, 2, 3, 4, 5)
print(x)
print(y)
print(z)
print(other)

print(my_tuple.count(5))
print(my_tuple.index(5))
print(len(my_tuple))