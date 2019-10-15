#Search by Moonlight
import random

#Abilities
class Ability:
    def __init__(self, name, power):
        self.name = name
        self.power = ability_power

    def attack(self):
        self.attack = random.randint(0, self.strength)
        self.max_damage = 1500
        #Return the Value
        return self.attack

# Weapons
class Weapon(Ability):
    def __init__(self, name, type, strength):
        super().__init__(name, power)
        self.name = weapon_name
        self.type = weapon_type
        #Inital Strength
        self.strength = 10

    def attack(self):
        self.attack_value = random.randint(0, 1500)
        # TODO: Use what you learned to complete this method.
        damage = random.randint(0, self.attack_value)
        return damage // 2

# Armor
class Armor:
    def __init__(self, name, type, protection):
        self.name = armor_name
        self.type = armor_type
        #Initial Protection
        self.protection = 10

#Generic Actor Class
class Actor:
    def __init__(self, name, age, starting_hp, starting_atk, starting_def):
        self.name = actor_name
        self.age = actor_age
        #Stats
        self.starting_hp = starting_hp
        self.starting_atk = starting_atk
        self.starting_def = starting_def
        #Inventory
        self.abilities = []
        self.armors = []
        self.weapons = []
        #Misc
        self.important_NPC = False #(Set to True so they cannot die, False for able to die.)
        self.boss = False #(Set to True when they are marked as a boss, False by default.)

class Protagonist(Actor):
    super().__init__(name, age, starting_hp, starting_atk, starting_def)
    self.name = protag_name
    self.age = protag_age
    self.starting_hp = starting_hp
    self.starting_atk = starting_atk
    self.starting_def = starting_def
    #Skill Levels
    self.cooking_level = 0
    self.smithing_level = 0
    self.mining_level = 0
    #


















if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    #Exposition
    print("Welcome!")
