is_old = "hello"
is_licensed = 5
print(bool("hello"))
print(bool(5))
print(bool(""))
print(bool(0))
print(bool({"key": "value"}))
print(bool([]))


if (is_old and is_licensed):
    print("Baby, you can drive my car.")
elif (is_old ):
    print("You're old enough, but you need a license.")
elif(is_licensed):
    print("You must be 18 years old to drive.")
else:
    print("You've got some aging and licensing to do.")