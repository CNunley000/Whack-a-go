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

def load_images(size):
    """loads in the go images"""
    global black
    global white
    global empty
    black = tk.PhotoImage(file='Whack-a-go/goBLACK.png')
    white = tk.PhotoImage(file='Whack-a-go/goWHITE.png')
    empty = tk.PhotoImage(file='Whack-a-go/goEMPTY.png')
    black = black.zoom(size)
    white = white.zoom(size)
    empty = empty.zoom(size)

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

    if stuff == 'main':
        window.destroy()
        win_main()

    else:
        key = stuff[0]
        i = stuff[1]
        #value = eval(f'{where}.get("1.0","end-1c")') 
        value = eval(f'new_setting{i}.get("1.0","end-1c")')
        settings[key] = value
        print(f"{key} = {value}")

        write_settings(file_name,['Zoom or Shrink', settings['Zoom or Shrink'], 'Zoom Amount', settings['Zoom Amount'], 'Sensei', settings['Sensei']])

def return_to_menu():
    """returns user to main menu NOT NEEDED if I put window.destroy at beginning of win_ functions"""
    global window
    
    window.destroy()

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
def create_board(blackPts,whitePts,size=19):
    """Creates inital board set up in A 2d List"""
    board = []
    
    for x in range(size):
        board.append([])
        for y in range(size):
            if f"({x},{y})" in blackPts:
                board[x].append('b')
            elif f"({x},{y})" in whitePts:
                board[x].append('w')
            else:
                board[x].append(' ')

    return(board)

def play(board,changes):
    """changes 2d board list"""
    for change in changes:
        change = eval(change)
        color = change[0]
        x = int(change[1][0])
        y = int(change[1][1])

        board[x][y] = color
    return(board)

def place(board):
    """takes a 2d list and generates the playable board WINDOW"""
    for row in range(0,len(board)):
        for col in range(0,len(board)):
            current = board[col][row]
            if current == 'b': # black stone
                globals()[f"{row}x{col}"] = tk.Button(window,image=black, command=lambda :wrong())
                globals()[f"{row}x{col}"].grid(column=col,row=row)
            elif current == 'w': # white stone
                globals()[f"{row}x{col}"] = tk.Button(window,image=white, command=lambda :wrong())
                globals()[f"{row}x{col}"].grid(column=col,row=row)
            elif current == ' ': # empty point
                globals()[f"{row}x{col}"] = tk.Button(window,image=empty, command=lambda :wrong())
                globals()[f"{row}x{col}"].grid(column=col,row=row)
            elif current == 'x': # correct next move
                globals()[f"{row}x{col}"] = tk.Button(window,image=empty, command=lambda :right())
                globals()[f"{row}x{col}"].grid(column=col,row=row)



def take_turn(board):
    """Updates the current board window """
    for row in range(0,len(board)):
        for col in range(0,len(board)):
            current = board[col][row]
            if current == 'b': # black stone
                globals()[f"{row}x{col}"]['image']= black
                globals()[f"{row}x{col}"]['command']=lambda :wrong()
            elif current == 'w': # white stone
                globals()[f"{row}x{col}"]['image']= white
                globals()[f"{row}x{col}"]['command']=lambda :wrong()
            elif current == ' ': # empty point
                globals()[f"{row}x{col}"]['image']= empty
                globals()[f"{row}x{col}"]['command']=lambda :wrong()
            elif current == 'x': # correct next move
                globals()[f"{row}x{col}"]['image']= empty
                globals()[f"{row}x{col}"]['command']=lambda :right()


def wrong():
    """What happens when wrong button is pressed"""
    print('Wrong Button')

def right():
    """Correct Button is pressed, must move game forward"""
    global turn_num
    global board
    turn_num += 1
    if turn_num > len(turn_list) - 1:
        print('you win')
    
    else:
        board = play(board,turn_list[turn_num])
        take_turn(board)


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
        globals()[f"lambda_vars{i}"] = [(setting),f'{i}']
        update = tk.Button(height=1, width=10, text=setting, command= lambda b=globals()[f"lambda_vars{i}"]:settings_button(b))
        update.grid(column=0,row=i)
        i +=1

        new_button = tk.Button(height=1, width=20, text='Main Menu',command = lambda b='main' :settings_button(b))
        new_button.grid(column=0,row=10,columnspan=2)

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
    global window
    global turn_num
    global turn_list
    global board

    window = tk.Tk()
    window.title('goban')

    load_images(settings['Zoom Amount'])

    with open(problem,'r') as file: # loads  in file, and sets up board, then sets up turns into a list
        reader = csv.reader(file,delimiter=',')
        turn_list = []
        i = 0
        for turn in reader:
            if i == 0:
                board = create_board(turn[0],turn[1],int(turn[2]))
        
            else:
                turn_list.append(turn)

            i += 1


    turn_num = 0
    board = play(board,turn_list[turn_num])
    place(board)




####################
# ACTUALLY RUNNING #
####################

win_welcome()

tk.mainloop()