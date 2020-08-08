username = input("Select a username.\n")
password = input("Now choose a password.\n")
pw_length = len(password)
secret = "*" * pw_length

print(f"{username}, your password {secret} is {pw_length} characters long.")
