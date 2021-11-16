# (weather = 'It's sunny') doesn't work
# (weather = "It's "kind of" sunny") doesn't work
weather = "It\'s \\kind of\\ sunny" 
print(weather)

# \t designates a tab
weather = "\t It\'s \\kind of\\ sunny"
print(weather)

# \n designates a new line
weather = "It\'s \\kind of\\ sunny \n I hope you have a good day." 
print(weather)