# int/float

# addition
print(2+4)
print(type(2 + 4))

# subtraction
print(2 - 4)
print(type(2 - 4))

# multiplication
print(2 * 4)
print(type(2 * 4))

# division
print(2 / 4)
print(type(2 / 4))

# zero is an integer, as it has no decimal values
print(0)
print(type(0))

# the sum of an integer and a float is a float
print(20 + 1.1)
print(type(20 + 1.1))

# the sum of two floats is a float, even if the decimal value is 0
print(9.9 + 1.1)
print(type(9.9 + 1.1))

# exponent = ** = x ^ y
print(2 ** 2)
print(2 ** 3)
print(2 ** 4)
print(2 ** 5)

# floor division = // = x / y rounded down to nearest integer
print(4 // 3)
print(14 // 5)

# modulo = % = remainder of x / y
print(10 % 4)
print(101 % 10)
print(1000 % 120)

# round
print(round(3.1))
print(round(3.5))

# absolute value
print(abs(20))
print(abs(-20))

# operator precedence (PEMDAS)
# ()
# **
# * /
# + -

# bin() translates numbers into binary notation, preceded by "0b" indicator
print(bin(1))
print(bin(2))
print(bin(3))
print(bin(4))
print(bin(5))

# to translate from binary, use int() with 2 as second argument
print(int("0b1", 2))
print(int("0b10", 2))
print(int("0b11", 2))
print(int("0b100", 2))
print(int("0b101", 2))