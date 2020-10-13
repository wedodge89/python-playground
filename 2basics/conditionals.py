is_old = False
is_licensed = True

print("Check check")

if is_old:
    print("You are old enough to drive.")
    if is_licensed:
        print("You have a drivers license.")
    else:
        print("You may be old enough, but you aren't licensed.")
elif is_licensed:
    print("How did you get a license, you whippersnapper?")
else:
    print("No dice, bro.")

# Alternative approach:
# if is_old and is_licensed:
#     print("You can drive.")
# elif is_old and not is_licensed:
#     print("Age ain't everything.")
# elif is_licensed and not is_old:
#     print("That must be a fake license.")
# else:
#     print("You need to grow up and get a license.")


