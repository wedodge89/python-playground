# T
print(True == 1)
# F
print("" == 1)
# F
print([] == 1)
# T
print(10 == 10.0)
# T
print([] == [])

# F
print(True is 1)
# F
print("" is 1)
# F
print([] is 1)
# F
print(10 is 10.0)
# F
print([] is [])

# "==" checks equality, while "is" checks location in memory