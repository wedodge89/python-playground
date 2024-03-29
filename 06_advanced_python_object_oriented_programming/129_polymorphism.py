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

def player_attack(char):
    char.attack()

wizard1 = Wizard("Merlin", 50)
archer1 = Archer("Robin", 100)

player_attack(wizard1)
player_attack(archer1)