def super_func(*args, **kwargs):
    total = 0
    print(args, kwargs)
    for items in kwargs.values():
        total += items
    return sum(args) + total

print(super_func(1, 2, 3, 4, 5, num1 = 5, num2 = 10))

# Rule: params, *args, default params, **kwargs