total = 0

def count():
    global total 
    total += 1
    return total

count()
count()
print(count())

total2 = 0

def count2(total2):
    total2 += 1
    return total2

print(count2(count2(count2(total2))))