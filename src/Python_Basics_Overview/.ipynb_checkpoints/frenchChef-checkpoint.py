#You can have inheritance in this classes. first you import the class
from Chef import Chef
class FrenchChef(Chef):
    def make_croissant(self):
        print("The chef makes croissants")
    def make_stake_tartare(self):
        print("The French chef can make a French stake tartare")