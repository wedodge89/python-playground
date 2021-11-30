is_old = True
is_licensed = True

if (is_old & is_licensed):
    print("Baby, you can drive my car.")
elif (is_old ):
    print("You're old enough, but you need a license.")
elif(is_licensed):
    print("You must be 18 years old to drive.")
else:
    print("You've got some aging and licensing to do.")


is_old = True
is_licensed = False
if (is_old and is_licensed):
    print("Baby, you can drive my car.")
elif (is_old ):
    print("You're old enough, but you need a license.")
elif(is_licensed):
    print("You must be 18 years old to drive.")
else:
    print("You've got some aging and licensing to do.")

is_old = False
is_licensed = True
if (is_old and is_licensed):
    print("Baby, you can drive my car.")
elif (is_old ):
    print("You're old enough, but you need a license.")
elif(is_licensed):
    print("You must be 18 years old to drive.")
else:
    print("You've got some aging and licensing to do.")

is_old = False
is_licensed = False
if (is_old and is_licensed):
    print("Baby, you can drive my car.")
elif (is_old ):
    print("You're old enough, but you need a license.")
elif(is_licensed):
    print("You must be 18 years old to drive.")
else:
    print("You've got some aging and licensing to do.")