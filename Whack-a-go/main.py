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

def set_settings(path):
    """looks for settings file then returns DICT"""
    global settings
    
    settings = {}

    with open(path, 'r') as file:
        i = 1
        for line in file.readlines(): # alternates between key value ie : [zoom][y]
            line = line.strip()
            if even(i) == True:
                value = line
                settings[key] = value
            elif even(i) == False:
                key = line
            i += 1

        print(settings)


def even(num):
    """checks if num is even or not T/F"""
    if num/2 == int(num/2):
        return(True)
    else:
        return(False)

def  write_settings(path,settings_list=['Zoom or Shrink','Zoom','Zoom Amount','1','Sensei','Cat']):
    """creates settings file and writes into the FILE"""
    with open(path, 'w') as s_file:
        
        for line in settings_list:
            s_file.write(f"{line}\n")

    set_settings(path)

#########################
# window specific FUNCS #
#########################

# functions that will only be used in specific windows (usualy to progress to next window)

# WELCOME
def test_name(where):
    """WELCOME SPECIFIC Retrieves input from text box"""
    global name
    global file_name
    global settings

    name=where.get("1.0","end-1c")
    print(name)

    file_name = f"{name}_settings.txt"

    if os.path.exists(file_name) == True: # settings file already exists
        window.destroy()
        set_settings(file_name)
        print(settings)
        win_main()

    else:
        window.destroy()
        write_settings(file_name)
        win_settings()
        


# SETTINGS
def settings_button(stuff):
    """Because of LAMDA in button variables need to be passed through in stuff list lol. Settings button, sets a new key value as determined by button"""
    global settings

    key = stuff[0]
    where = stuff[1]
    value = globals()[where]
    settings[key] = value.get("1.0","end-1c")
    print(f"{key} = {value}")

# MAIN
def main_button(command='Button Not set'):
    """This will handle the button inputs in main_button"""
    if command == 'settings':
        window.destroy()
        win_settings()

    elif os.path.exists(command) == True:
        window.destroy()
        win_game(command)
    else:
        print(f"err : {command}")

# GAME


# SENSEI
    


###########
# WINDOWS #
###########

# window creating functions

# welcome 
    # this will welcome player and get global variable usr_name
    # if name_settings exists than load main menu, else create file and load settings menu
def win_welcome():
    """loads welcome window"""
    global window
    global name

    window = tk.Tk()
    window.title("welcome")
    window.geometry("400x400")


    name_box = tk.Text(height=1,width=10)
    name_box.grid(row=1,column=1,columnspan=3)
    enter = tk.Button(height=1, width=10, text="Enter", command= lambda b=name_box :test_name(b))
    enter.grid(row=2,column=3)


# settings
    # this can be called througout use, 
    # it will get info like 
        # zoom or shrink (and how much)
        # sensei preference
        # more
    # this will write into settings file the usrs settings
def win_settings():
    """Settings window"""
    global window
    global settings

    window = tk.Tk()
    window.title("settings")
    window.geometry("400x600")

    i = 0

    print(settings)

    for setting in settings.keys():
        globals()[f"new_setting{i}"] = tk.Text(height=1,width=10)
        globals()[f"new_setting{i}"].grid(column=1,row=i)
        globals()[f"lambda_vars{i}"] = [(setting),f'new_settting{i}']
        update = tk.Button(height=1, width=10, text=setting, command= lambda b=globals()[f"lambda_vars{i}"]:settings_button(b))
        update.grid(column=0,row=i)
        i +=1


# main menu
    # This will give the option to start the game or go to settings menu
def win_main():
    """main menu window"""
    global window
    
    window = tk.Tk()
    window.title("main menu")
    window.geometry("800x600")

    settings_button = tk.Button(height=1, width=10, text="Settings", command= lambda b='settings' :main_button(b))
    settings_button.pack()

    problems = ['problem_1','problem_2']

    for problem in problems:
        if problem.lower() == 'you':
            window.destroy()
            print('I got 99 problems and you AINT one >:(')
            assert(False)
        else:
            button = tk.Button(height=1, width=10, text=problem, command= lambda b=f'{problem}.csv' :main_button(b))
            button.pack()

 
#  main game
    # this will provide the majority of the actual gameplay
    # loading the next move when they get the correct answer
def win_game(problem):
    """Actual tsumego window"""
    print('game')


# sensei window
    # this is a window with a semi-animated 'sensei' who will react to the user's sucess
def win_sensei():
    """Sensei top window"""
    print('sensei')


####################
# ACTUALLY RUNNING #
####################

win_welcome()

tk.mainloop()