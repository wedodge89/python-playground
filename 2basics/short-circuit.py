# Short Circuiting
# Short Circuiting is just using the appropriate conditional ('and' or 'or', depending on circumstances, to make your code more performant.)
is_Friend = True
is_User = True

if is_Friend and is_User:
    print("Best friends forever.")

if is_Friend or is_User:
    print("BFFs!")
