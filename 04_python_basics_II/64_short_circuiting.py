# increase performance by using appropriate and/or
# OR short circuits when first statement is true
# AND short circuits when first statement is false

is_friend = True
is_user = True

if is_friend or is_user:
    print("Best friends forever.")