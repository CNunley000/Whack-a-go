# Conner Nunley
# A3
# This is gonna write my csvs

import csv

with open('problem_1.csv','w+') as file:
    writer = csv.writer(file,delimiter=',')
    # 0th line
        # This line will be BlackPTS,WhitePTS,size
    line = []
    blackpts = []
    whitepts = []
    i = 0 # black counter
    while True: # makes black
        x = input(f'{i}th black x value')
        if x == 'done':
            break
        y = input(f'{i}th black y value')

        blackpts.append(f"({x},{y})")
        i += 1

    print(blackpts)
    i = 0 # white counter
    while True: # makes white
        x = input(f'{i}th white x value')
        if x == 'done':
            break
        y = input(f'{i}th white y value')

        whitepts.append(f"({x},{y})")
        i += 1
 

    line = [blackpts,whitepts,19] 
    
    writer.writerow(line) # writes the 0th line

    # All other lines

    colors = ['b','y','x','e']
    turnnum = 0
    while True:
        line = []

        while True:
            color = input('color')

            x = input('x')
            y = input('y')

            current = [color,[x,y]]

            line.append(current)
            print(current)
            done = input(f"done? Turn #{turnnum}\nline = {line}\nY/N")

            if done == 'Y':
                break
        writer.writerow(line)
       
        done = input("done?")
        turnnum+=1
        if done == 'Y':
            break
