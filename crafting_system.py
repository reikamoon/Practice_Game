from classes import *

# CRUD Resources
#Create Food/Weapon
#Read Food/Weapon
#Update Food/Weapon (Enhancing)
#Destroy Food/Weapon (Eating)

#Step 1
def Gather_Ore():
    #Test
    item_amount == 5
    item_name == "Iron Ore"
    print("Gathering resources...")
    print("Collected {0} {1}!".format(item_amount, item_name))
    self.add_item("Iron Ore", "Ore", 0)
    ingredients_for_sword = True

def Gather_Food():
    #Test
    item1_amount == 1
    item2_amount == 1
    item3_amount == 1
    item1_name == "Box of Noodles"
    item2_name == "Tomato"
    item3_name == "Cheese"
    print("Gathering resources...")
    print("Found {0} x {1}!".format(item1_name, item1_amount))
    print("Found {0} x {1}!".format(item2_name, item2_amount))
    print("Found {0} x {1}!".format(item3_name, item3_amount))
    self.add_item("Box of Noodles", "Food", 3)
    self.add_item("Tomato", "Food", 5)
    self.add_item("Cheese", "Food", 5)
    ingredients_for_spaghet = True

#Step 2
def Cook():
    #Test
    inventory = ['Tomato', 'Box of Noodles', 'Cheese']
    print("Time to Cook!")
    if ingredients_for_spaghet == True:
        print("Let's make spaghetti!")
        print("Boiling water...")
        print("Cutting up veggies...")
        print("Spaghetti is done!")
    #Remove Items from List, Replace with new Item
        inventory.remove('Tomato')
        inventory.remove('Box of Noodles')
        inventory.remove('Cheese')
        self.add_item("Spaghetti", "Food", 50)
        print("Would you like to enhance your spaghetti? Currently heals 50 health. Y/N")
        user_input = user_input()
        if user_input == "Y":
            self.enhance_food()
    else:
        print("Not enough resources!")

#Optional Step 3
def enhance_food():
