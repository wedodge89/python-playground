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

