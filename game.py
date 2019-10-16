#Search by Moonlight
import random

#Start
print("Today was a rainy day.")
print("The clouds are dark, and the wind is howling.")
print("All is silent, save for the sound of the rain pitter pattering against my window.")
print("Today, I wanted to play, but...")
print("")
print("---------------------------------------------------------------------------------")
print("What is your name?")
protag_name = input()
if protag_name == "Reika":
    print("Reika. That name sounds familiar...")
else:
    print("{0}, such a lovely name.".format(protag_name))
print("{0}: ...".format(protag_name))
print("Mother: Daydreaming again, {0}?".format(protag_name))
print("{0}: ...!".format(protag_name))
print("Mother: Did I scare you? I am going to make a quick trip to your grandmother's.")
print("Mother: It is awfully pouring outside. Whatever you do, do not go outside.")
print("{0}: ...".format(protag_name))
print("With that, Mother left.")
print("")
print("---------------------------------------------------------------------------------")
print("{0}: Mother has been gone for a while now. I'm bored.".format(protag_name))
print("{0}: (What should I do?)".format(protag_name))
print("[A]: Play in Mother's Room")
print("[B]: Play in the Kitchen")
print("(Make a selection, A or B)")
