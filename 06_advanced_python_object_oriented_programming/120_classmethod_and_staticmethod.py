# OOP
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def shout(self):
        print("My name is {self.name}")

# use class method when concerned with attributes of an object 
    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

# use static method when attributes are not needed/important
    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2


player1 = PlayerCharacter("Aliot", 32)
player2 = PlayerCharacter("Laarn", 30)

print(player1.adding_things(2, 3))
print(PlayerCharacter.adding_things(1,2))