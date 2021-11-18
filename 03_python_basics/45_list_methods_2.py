basket = ["a", "b", "c", "d", "e", "d"]

print(basket.index("b", 0, 3)) # return index of value between two given indexes
print("d" in basket) # return True is list contains item, False if not
print("x" in basket)
print("i" in "Elliott Dodge") # can also be used on strings
print(basket.count("d"))