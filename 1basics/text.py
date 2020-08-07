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
alphabet = "abcdefghij"
          # 0123456789

# [start:stop:stepover]
print(alphabet)
print(alphabet[0])
print(alphabet[1])
print(alphabet[0:2])
print(alphabet[3:5])
print(alphabet[0:10])
print(alphabet[0:10:2])
print(alphabet[-1])
print(alphabet[-2])
print(alphabet[::-1])
print(alphabet[::-2])

# immutability
# Strings can be changed in whole, but not in part.