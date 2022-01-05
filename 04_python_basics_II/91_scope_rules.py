a = 1
def parent():
    a = 10
    def confusion():
        return a
    return(confusion())

print(a)
print(parent())

# 1 - start with local
# 2 - parent local
# 3 - global
# 4 - built in python functions