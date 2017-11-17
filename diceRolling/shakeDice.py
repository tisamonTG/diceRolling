# create a program that simulates a dice roll
#
# Tisamon

print(" ***********************************************")
print(" ************** Roll the Dice ******************")
print(" ***********************************************")
print("\n")
print(" ")

import random


def start_rolling():
        print(" To roll the dice press 'R' and enter")
        print(" ")
        beginroll = input().format()

# print(beginRoll)


def ran_generate():
    select = random.randint(0,5)
    print("Here is :" + select)


start_rolling()
ran_generate()


if start_rolling() == "R":
    # Do something like a random number generator
    print(" Generate random num")

else:
    if start_rolling() == "Q":
        exit()

    else:
        print(" enter R for dice roll or Q to wuit the program")



