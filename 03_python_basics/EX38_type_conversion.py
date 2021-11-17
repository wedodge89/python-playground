name = "Elliott Dodge"
partner = "Lauren Dodge"
age = 31
relationship_status = "Engaged " 
print(name + ", age " + str(age) + ", is " + relationship_status + " to " + partner + ".")
relationship_status = "Married "
print(f"{name}, age {age}, is {relationship_status} to {partner}.")

birth_year = int(input("What year were you born? "))
is_older = str(input("Have you had a birthday this year? ")).lower()
current_year = 2021
if is_older == "y": 
    age = int(current_year - birth_year)
    print(f"Your age is {age}.")
elif is_older == "n":
    age = int(current_year - birth_year -1)
    print(f"Your age is {age}.")