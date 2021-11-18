amazon_cart = [
    "notebooks", 
    "sunglasses",
    "toys",
    "grapes"]
# print entire list
print(amazon_cart)
# print first two items
print(amazon_cart[0:2])
# print every other item, starting with first
print(amazon_cart[0::2])

# changing list items
amazon_cart[0] = "laptop"
print(amazon_cart[0])
print(amazon_cart)

# copying a list
new_cart = amazon_cart[:]
print(amazon_cart)
print(new_cart)