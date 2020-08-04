print(type("hello!"))
username = "wedodge"
password = "yeahright"
long_string = '''
WOW
O O
---
'''

print(long_string)

first_name = "Elliott"
last_name = "Dodge"
full_name = first_name + " " + last_name
print(full_name)

# type conversion
print(type(str(100)))

# escape sequence
# \t = tab
# \n = new line
weather = "\t It's \"kind of\" sunny. \n Have a great day."
print(weather)

# formatted strings
name = "Elliott"
age = 30

print("Hi, " + name + ". You are " + str(age) + " years old.")
print(f"Hi, {name}. You are {age} years old.")
print("Hi, {}. You are {} years old.".format("Elliott", "30"))
print("Hi, {}. You are {} years old.".format(name, age))
print("Hi, {1}. You are {0} years old.".format(age, name))

# string indexes