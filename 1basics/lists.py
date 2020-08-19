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
basket = [1, 2, 3, 4, 5]
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