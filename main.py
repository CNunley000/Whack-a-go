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

size = 1

black = black.zoom(size)
white = white.zoom(size)
empty = empty.zoom(size)

################
# create board #
################
def create_board(blackPts,whitePts,size=19):
    """Creates inital board set up in A 2d List"""
    board = []
    
    for x in range(size):
        board.append([])
        for y in range(size):
            board[x].append(y)

    return(board)

#####################################
# create specified changes to board #
#####################################

###########################
# generate playable board #
###########################
def place(bStarts,wStarts,size=19): # OUTDATED
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
    """changes 2d board list"""
    print("Hello World :)")

############
## SENSEI ##
############


##############
## Run Game ##
##############

goban = create_board(0,0)

print(goban)

tk.mainloop()