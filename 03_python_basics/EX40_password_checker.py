username = input("What is your username? ")
password = input("What is your password? ")

# replace characters in password with *s for security
password_length = len(password)
secret = "*" * password_length 

print(f"Your username is: {username}")
print(f"Your password ({secret}) is {password_length} charaters long.")
