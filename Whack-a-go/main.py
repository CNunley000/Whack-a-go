# Conner Nunley
# Comp Prog A3
# No cheating :)
# whack-a-go

# This will be a tsume go puzzle game using the principles and basics of a whack-a-mole game

# I will migrate my code to this new file as needed because I needed to reorganize, because... my old code was a mess

import tkinter as tk
import csv
import os



###################
# OTHER FUNCTIONS #
###################

# function for various purposes



###########
# WINDOWS #
###########

# window creating functions

# welcome 
    # this will welcome player and get global variable usr_name
    # if name_settings exists than load main menu, else create file and load settings menu
def win_welcome():
    """loads welcome window"""
    global welcome
    global name

    welcome = tk.Tk()
    welcome.title("welcome")
    welcome.geometry("400x400")



# settings
    # this can be called througout use, 
    # it will get info like 
        # zoom or shrink (and how much)
        # sensei preference
        # more
    # this will write into settings file the usrs settings
def win_settings():
    """Settings window"""
    print("setting")


# main menu
    # This will give the option to start the game or go to settings menu
def win_main():
    """main menu window"""
    print('main')


# main game
    # this will provide the majority of the actual gameplay
    # loading the next move when they get the correct answer
def win_game():
    """Actual tsumego window"""
    print('game')


# sensei window
    # this is a window with a semi-animated 'sensei' who will react to the user's sucess
def win_sensei():
    """Sensei window"""
    print('sensei')


####################
# ACTUALLY RUNNING #
####################

win_welcome()