import random

class person:
    def __init__(self, name, hp, ip, atk, intimidate):
        self.name = name
        # health points
        self.hp = hp
        self.maxhp = hp
        # intimidation points
        self.ip = ip
        self.maxip = ip
        # highest attack value
        self.atk_high = atk +10
        # lowest attack value
        self.atk_low = atk -10
        # Options for action
        self.action = ["Bite", "Intimidate"]
        self.intimidate = intimidate

    def get_stat(self):
        """To print stats"""
        print(f"\t\t {self.name.upper()}")
        print(f"\t\t {self.hp}/{self.maxhp}")
        print(f"\t\t {self.ip}/{self.maxip}")
# Only need self. as everything can be accessed. Only need to add something else if more is needed
    def generate_dmg(self):
        """To randomly generate attack damage"""
        dmg = random.randrange(self.atk_low, self.atk_high)
        return dmg

    def take_damage(self, dmg):
        """To receive attack damage"""
        # the hp minus the damage dealt
        self.hp = self.hp - dmg
        # if health is below 0 it will equal 0 (to avoid negative)
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def choose_action(self):
        """Allows user to select act"""
        # number starts from 1
        number = 1
        print("\t\tACTION: ")
        for element in self.action:
            # each element within self.action defined above will be listed.
            print(f"\t\t\t{number}: {element}")
            number = number + 1

    def reduce_ip(self, cost):
        """calculate and reduce intimidation points"""
        self.ip = self.ip - cost
        return self.ip

    def choose_int(self):
        """To choose intimidation"""
        number = 1
        print("\t\t Choose intimidation tactic: ")
        print()
        for element in self.intimidate:
            print(f"\t\t {number}: {element.name}")
            number = number + 1
