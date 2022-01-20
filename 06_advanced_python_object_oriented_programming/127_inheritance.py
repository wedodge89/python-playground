class User():
    def sign_in(self):
        print(f"{self.name} logged in")

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"attacking with arrows. arrows left: {self.num_arrows}")

wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Robin", 100)
wizard1.sign_in()
wizard1.attack()
archer1.sign_in()
archer1.attack()

print(isinstance(wizard1, Wizard))
print(isinstance(wizard1, Archer))
print(isinstance(wizard1, User))
print(isinstance(wizard1, object))
print(isinstance(archer1, Wizard))
print(isinstance(archer1, Archer))
print(isinstance(archer1, User))
print(isinstance(archer1, object))