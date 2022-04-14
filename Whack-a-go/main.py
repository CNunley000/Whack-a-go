# Conner Nunley
# Comp Prog 2
# No Cheating :)

import tkinter as tk
import csv

window = tk.Tk()
window.title("goban")

# This will be a tsume go program that gives you predetermined tsume go problems and you must continue in the right order
# There will be a specified position to click, and if you click it the series will continue, with random 'Sensei' Responses in another window
# Sensei will be open in another window, they will be chosen before game

# create a photoimage variable
size = 1

black = tk.PhotoImage(file='goBLACK.png')
white = tk.PhotoImage(file='goWHITE.png')
empty = tk.PhotoImage(file='goEMPTY.png')
black = black.zoom(size)
white = white.zoom(size)
empty = empty.zoom(size)


def load_images(size):
    black = tk.PhotoImage(file='goBLACK.png')
    white = tk.PhotoImage(file='goWHITE.png')
    empty = tk.PhotoImage(file='goEMPTY.png')
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
            if f"({x},{y})" in blackPts:
                board[x].append('b')
            elif f"({x},{y})" in whitePts:
                board[x].append('w')
            else:
                board[x].append(' ')

    return(board)

#####################################
# create specified changes to board #
#####################################
def play(board,changes):
    """changes 2d board list"""
    print("Hello World :)")


###########################
# generate playable board #
###########################
def placeDUMB(bStarts,wStarts,size=19): # OUTDATED
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

def place(board):
    """takes a 2d list and generates the playable board WINDOW"""
    for row in range(0,len(board)):
        for col in range(0,len(board)):
            current = board[row][col]
            if current == 'b':
                black_stone = tk.Button(image=black)
                black_stone.grid(column=col,row=row)
            elif current == 'w':
                white_stone = tk.Button(image=white)
                white_stone.grid(column=col,row=row)
            else:
                point = tk.Button(image=empty)
                point.grid(column=col,row=row)
                

##############
## Problems ##
##############

t1 = {'black':[0,1],'white':[0,1],'next':[0,1]]

############
## SENSEI ##
############

# Create settings

# read settings

##############
## Run Game ##
##############

black_list = ["(0,0)"]
white_list = ["(3,3)"]

board_list = create_board(black_list,white_list)


place(board_list)


tk.mainloop()