#!/usr/bin/env python3

"""
Deadline:
Friday

Pseudo Code

1 make square 20 x 20 asterisc long *
2 each asterisc is a random number  *    
3 limit random number from 1 to 10   *  
4 the asteriscs around the one picked are to be taken out *
5 random asteriscs are mines, if one's hit, game over
"""

import random
import numpy as np


class Main:

    blueprint = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(20):
        new = blueprint
        new[i].append('M')
        for i in range(20):
            new = blueprint
            new[i].append('M')
    
    def verifier(num):
        num = int(num)
        if num > 20:
            raise Exception("Error number should be smaller than 20")
        elif num < 0:
            raise Exception("Error number should be bigger than 0")
        else:
            return num
    
    def randomnum():
        for i in range(10):
            i += 1
            i+1
            randnum = random.randint(1,i)
        return randnum

# --------------------------------------

star = Main.blueprint
    

def surround(y,x):
    ran = Main.randomnum()
    if x + ran > 19 or y + ran >19:
        for i in range(ran):
            x -= 1
            star[y][x] = '░'
        for i in range(ran):
            y -= 1
            star[y][x] = '░'
        for i in range(ran):
            x -= 1
            y -= 1
            star[y][x] = '░'
    elif x + ran < 19 or y + ran < 19:
        for i in range(ran):
            x += 1
            star[y][x] = '░'
        for i in range(ran):
            y += 1
            star[y][x] = '░'
        for i in range(ran):
            x += 1
            y += 1
            star[y][x] = '░'

def background(y,x):
    y = int(y)
    x = int(x)
    star[y][x]= '■'
    surround(y,x)
    print("""
███╗░░░███╗██╗███╗░░██╗███████╗░██████╗░██╗░░░░░░░██╗███████╗███████╗██████╗░███████╗██████╗░
████╗░████║██║████╗░██║██╔════╝██╔════╝░██║░░██╗░░██║██╔════╝██╔════╝██╔══██╗██╔════╝██╔══██╗
██╔████╔██║██║██╔██╗██║█████╗░░╚█████╗░░╚██╗████╗██╔╝█████╗░░█████╗░░██████╔╝█████╗░░██████╔╝
██║╚██╔╝██║██║██║╚████║██╔══╝░░░╚═══██╗░░████╔═████║░██╔══╝░░██╔══╝░░██╔═══╝░██╔══╝░░██╔══██╗
██║░╚═╝░██║██║██║░╚███║███████╗██████╔╝░░╚██╔╝░╚██╔╝░███████╗███████╗██║░░░░░███████╗██║░░██║
╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝╚═════╝░░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝
    """)
    for i in range(len(star)):
        array = star
        print(array[i])
    print("""
╭━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━╮
╰━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━╯
    """)


def find(lst):
    new_lst = np.array(lst)
    var = '░'
    indices = np.where(new_lst == var)
    result = list(zip(indices[0],indices[1]))
    output = []
    for element in result:
        output.append(list(element))
    print(output)
    



def shot():
    y = input("Select by coordinate Y: (from 19 to 0)\n")
    y = Main.verifier(y)
    x = input("Select by coordinate X: (from 20 to 0)\n")
    x = Main.verifier(x)
    background(y,x)
    find(star) 
    
  

shot()



while True:
    ans = input("Another one? [y] [n]\n")
    if ans == 'y':
        shot()
    elif ans == 'n':
        print("Goodbye!")
        break



