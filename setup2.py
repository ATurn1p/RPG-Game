import random
# creating class of intimidate
class Intimidate:
# defining the class of intimidate
    def __init__(self, name, i_cost, damage, i_type):
        # e.g Bark
        self.name = name
        # 10
        self.i_cost = i_cost
        # 100
        self.damage = damage
        # dark
        self.i_type = i_type

    def generate_i_damage(self):
        # lower possibility for damage e.g. 100 - 15 = 80
        low = self.damage - 15
        # Higher possibility for damage e.g. 100 + 15 = 115
        high = self.damage + 15
        # To randomise the damage dealt between the low and high figure
        damage = random.randint(low, high)
        return damage
