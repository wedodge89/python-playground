basket = [1, 2, 3, 5, 4]

# adding
basket.append(6) # to the end
print(basket)
basket.insert(5, 7) # at a given index
print(basket)
basket.extend([8, 9, 100, 101]) # add a list to the end
print(basket)

# removing
basket.pop() # last item the list (or at given index), returning that item 
print(basket)
basket.remove(100) # the given value
print(basket)
new_basket = basket[:]
new_basket.clear() # all items
print(new_basket)