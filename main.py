# Conner Nunley
# Comp Prog 2
# No Cheating :)

import tkinter as tk

window = tk.Tk()
window.title("goban")

# This will be a tsume go program that gives you predetermined tsume go problems and you must continue in the right order
# There will be a specified position to click, and if you click it the series will continue, with random 'Sensei' Responses in another window
# Sensei will be open in another window, they will be chosen before game

# create a photoimage variable
black = tk.PhotoImage(file='goBLACK.png')
white = tk.PhotoImage(file='goWHITE.png')
empty = tk.PhotoImage(file='goEMPTY.png')
black = black.zoom(2)
white = white.zoom(2)
empty = empty.zoom(2)

################
# create board #
################
def create_board(blackPts,whitePts,size=19):
    """Creates inital board set up"""

#####################################
# create specified changes to board #
#####################################

###########################
# generate playable board #
###########################
def place(bStarts,wStarts,size=19):
    """This is given starting positions and outputs a board OUTDATED METHOD I THINK"""
    for x in range(size):
        for y in range(size): 
            # based on 'color' create button
            if f"({x},{y})" in bStarts:
                black_stone = tk.Button(image=black)
                black_stone.grid(column=x,row=y)
            elif f"({x},{y})" in wStarts:
                white_stone = tk.Button(image=white)
                white_stone.grid(column=x,row=y)
            else:
                point = tk.Button(image=empty)
                point.grid(column=x,row=y)

def place_on_board(board):
    """takes a 2d list and generates the playable board"""
    print("temp message")

def play_on_board(board,changes):
    """Takes 2d board list and then makes changes"""
    print("Hello World :)")

############
## SENSEI ##
############


##############
## Run Game ##
##############

x = ['(0,0)']
y = ['(2,2)']

place(x,y,0)

tk.mainloop()