my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 0

# my work
for item in my_list:
    x += 1
print(x)
# in my defense, my understanding is that the final value should be the length of the list. guess I didn't pay enough attention. whoops. the logic is there.

# answer key
counter = 0
for item in my_list:
    counter = counter + item
print(counter)