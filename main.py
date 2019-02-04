from setup1 import person
from setup2 import Intimidate
import random
# recalling the classes and provding the arguments and values
stare = Intimidate("Stare", 10, 100, "dark")
growl = Intimidate("Growl", 12, 120, "dark")
bark = Intimidate("Bark", 40, 200, "dark")
# creating a list
int_list = [stare, growl, bark]

# creating the actors and their stats
player1 = person("Ida", 500, 100, 50, int_list)
enemy1 = person("Rival Dog", 800, 70, 30, int_list)

print("=====================================================")
print("\tWelcome to Ida's Dog Walk")
print()
print("\tLet's secure Ida's territory!")
print()
player1.get_stat()
print()
enemy1.get_stat()
print()
print("=====================================================")
# creating the loop to allow continued attacks until one wins
running = True
while running:
    print("=====================================================")
    print(f"\t {player1.name.upper()}")
    # asks the user to choose an action
    player1.choose_action()
    print()
    choice_input = input("\t\tChoose a number: ")
    index = int(choice_input) - 1
    #
    print()
    print(f"\t You chose {player1.action[index]}")
    print()

    if index == 0:
        dmg = player1.generate_dmg()
        enemy1.take_damage(dmg)
        print(f"\t You bit {enemy1.name} and dealt {dmg} amount of damage")
        print()

    if index == 1:
        player1.choose_int()
        print()
        int_choice = int(input("Choose your intimidation: "))
        int_index = int_choice - 1

        intimidate = player1.intimidate[int_index]
# Below recalls the function generate_i_damage and works under the variable int_damage
        int_damage = intimidate.generate_i_damage()
        int_name = intimidate.name
        int_cost = intimidate.i_cost

        if int_cost > player1.ip:
            print("Not enough intimidation points")
            continue
        else:
            player1.reduce_ip(int_cost)
            enemy1.take_damage(int_damage)
            print("=====================================================")
            print(f"You attacked with {int_name} and dealt {enemy1.name} {int_damage} damage")
    # else:
    #     print("Please choose a correct number!")
    #     continue

    print("=====================================================")
    print(f"\t {enemy1.name.upper()}")
    print()
    enemy1_choice = random.randrange(0, len(enemy1.action))
    if enemy1_choice == 0:
        enemy1_dmg = enemy1.generate_dmg()
        player1.take_damage(enemy1_dmg)
        print(f"\t {enemy1.name.capitalize()} attacked you causing {enemy1_dmg} damage")
    print()
    player1.get_stat()
    print()
    enemy1.get_stat()
    print()
    if player1.hp == 0:
        print("\t\t Oh no, you lost!")
        running = False
    elif enemy1.hp == 0:
        print("\t\t Ida's territory is safe...for now!")
        running = False
