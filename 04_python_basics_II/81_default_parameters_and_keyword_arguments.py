# default parameters
def say_hello(name = "Darth Vader", emoji= ">:-("):
    print(f"hello {name} {emoji}")
say_hello()

# positional arguments are dependent on position
say_hello("Andrei", ":)")
say_hello("Elliott", ":-D")
say_hello("Lauren", "XD")

# keyword arguments are not dependent on position <-not best practices
say_hello(emoji = ";-)", name = "Indy")
say_hello("Mo")