is_magician = False
is_expert = False

print("Magician: " + str(is_magician))
print("Expert: " + str(is_expert))
if is_magician and is_expert:
    print("You are a master magician!")
elif is_magician and not is_expert:
    print("At least you're getting there.")
else:
    print("You need magic powers.")
