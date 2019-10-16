#Search by Moonlight
import random

#Abilities
class Ability:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        self.attack = random.randint(0, self.strength)
        self.max_damage = 1500
        #Return the Value
        return self.attack

# Weapons
class Weapon(Ability):
    def __init__(self, name, type, strength):
        super().__init__(name, power)
        self.name = name
        self.type = type
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
        self.name = name
        self.type = type
        #Initial Protection
        self.protection = 10

     def defend(self):
        self.defense_value = random.randint(0,1500)
        self.max_block = 1500
        return self.defense_value

#Generic Actor Class
class Actor:
    def __init__(self, name, age, starting_hp, starting_atk, starting_def):
        self.name = name
        self.age = age
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

#Protagonist
class Protagonist(Actor):
    def __init__(self, name, age, starting_hp, starting_atk, starting_def):
        super().__init__(self, starting_hp, starting_atk, starting_def)
    self.name = name
    self.age = age
    self.starting_hp = starting_hp
    self.starting_atk = starting_atk
    self.starting_def = starting_def
    #Skill Levels
    self.cooking_level = 0
    self.smithing_level = 0
    self.mining_level = 0

    def add_ability():
        self.abilities.append(ability)

    def add_armor():
        self.armors.append(armor)

    def add_weapon():
        self.weapons.append(weapon)

     def attack(self):
        total = 0
        for ability in self.abilities:
            total += ability.attack()
        return total

    def defend(self, damage_amt):
        total_armor = 0
        for armor in self.armors:
            block = armor.block()
            total_armor = total_armor + block
        return sum

    def take_damage(self, damage):
        self.current_health = self.current_health - damage - self.defense_value
        return self.current_health
        print("Took damage! Remaining health: {0}".format(self.current_health))

    def is_alive(self):
        if self.current_health < 0:
            return False
        else:
            return True

    def fight(self, opponent):
        while self.is_alive() == True and opponent.is_alive() == True:
            if len(self.abilities) == 0 and len(opponent.abilities) == 0:
                print("{0} and {1} both lack abilities! It's a draw!".format(self.name, opponent.name))
                break
            damage = self.attack()
            opponent_damage = opponent.attack()
            print("Battle Start!")
            print("{0} vs. {1}!".format(self.name, opponent.name))

            # opponentdamage = opponent.attack()
            # opponent.take_damage(damage)
            # self.take_damage(opponentdamage)

#Enemy
class Enemy:
    def __init__(self, name, level, hp, atk, defense):
        self.name = name
        self.level = level
        self.hp = hp
        self.atk = atk
        self.defense = defense
        #Special
        self.boss = False #(Set to True when they are marked as a boss, False by default.)
























if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    #Exposition
    print("Welcome!")
