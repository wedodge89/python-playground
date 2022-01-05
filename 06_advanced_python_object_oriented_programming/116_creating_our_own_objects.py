# OOP
class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("run")

player1 = PlayerCharacter("Aliot", 32)
player2 = PlayerCharacter("Laarn", 30)

print(player1.name)
print(player1.age)
print(player2.name)
print(player2.age)