amazon_cart = ["notebooks", "sunglasses", "orange juice", "toys", "grapes"]
print(amazon_cart[0])
print(amazon_cart[1])
print(amazon_cart[2])

# List slicing
print(amazon_cart[0:2:1])
print(amazon_cart[0::2])

amazon_cart[0] = "binders"
print(amazon_cart[0:3])
print(amazon_cart)

# Matrix
# Essentially a list of lists
matrix = [
    [1, 2, 3],
    [2, 4, 6],
    [7, 8, 9]
]

# I typically use spaces to keep things cleaner/clearer, but didn't use space here to illustrate the image
x_matrix = [
    [1,0,1],
    [0,1,0],
    [1,0,1]
]

print(matrix[0][2])
print(matrix[1][2])
print(matrix[2][0])

# List methods
basket = [1, 2, 3, 4, 5, 7, 6]
print(len(basket))
print(basket)
# add one item to end of list
print(basket.append(6))
print(basket)
# inset value of y at index x
basket.insert(4, 100)
print(basket)
# add multiple items (as a list)
basket.extend([100, 101])
print(basket)
# remove last item
# Note: pop() returns the item removed
basket.pop()
print(basket)
basket.pop()
print(basket)
# remove item @ index
basket.pop(0)
print(basket)
# remove value
basket.remove(4)
print(basket)
# print index
print(basket.index(2))
# find value in list
print(2 in basket)
print("i" in "Elliott")
# count number of times value occurs in list
print(basket.count(2))
# sorts the list (mutates, doesn't return)
basket.sort()
print(basket)
# sorts and returns new list
print(sorted(basket))
# copies list into new list
new_basket = basket.copy()
print(new_basket)
# reverses the order of a list
basket.reverse()
print(basket)