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
    
    def randomnum(x):
        for i in range(x):
            i += 1
            i + 1
            randnum = random.randint(1,i)
        return randnum

# --------------------------------------

star = Main.blueprint
    
def lefting(z):
    ran = Main.randomnum(10)
    if z + ran > 20:
        for i in range(ran):
            z -= 1
        return z

def surround(y,x):
    ran = Main.randomnum(10)
    if x + ran > 20 and y + ran > 19:
        for i in range(ran):
            while x and y > 0 and x < 20 and y < 19:
                x -= 1
                star[y][x] = '░'
        for i in range(ran):
            while y and x > 0:
                y -= 1
                star[y][x] = '░'
        for i in range(ran):
            while x and y > 0 and x < 20 and y < 19:
                x -= 1
                y -= 1
                star[y][x] = '░'
    elif x + ran < 20 and y + ran < 19:
        for i in range(ran):
            while x < 20 and y < 19:
                x += 1
                star[y][x] = '░'
        for i in range(ran):
            while y < 19 and x < 20:
                y += 1
                star[y][x] = '░'
            while y < 19 and x < 20:
                for i in range(ran):
                    x += 1
                    y += 1
                    star[y][x] = '░'

def background(y,x):
    y = int(y)
    x = int(x)
    star[y][x]= '■'
    surround(y,x)
#------------------------------------------------------------------------------------------
    print("""
███╗░░░███╗██╗███╗░░██╗███████╗░██████╗░██╗░░░░░░░██╗███████╗███████╗██████╗░███████╗██████╗░
████╗░████║██║████╗░██║██╔════╝██╔════╝░██║░░██╗░░██║██╔════╝██╔════╝██╔══██╗██╔════╝██╔══██╗
██╔████╔██║██║██╔██╗██║█████╗░░╚█████╗░░╚██╗████╗██╔╝█████╗░░█████╗░░██████╔╝█████╗░░██████╔╝
██║╚██╔╝██║██║██║╚████║██╔══╝░░░╚═══██╗░░████╔═████║░██╔══╝░░██╔══╝░░██╔═══╝░██╔══╝░░██╔══██╗
██║░╚═╝░██║██║██║░╚███║███████╗██████╔╝░░╚██╔╝░╚██╔╝░███████╗███████╗██║░░░░░███████╗██║░░██║
╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝╚═════╝░░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝
    """)
#------------------------------------------------------------------------------------------
    for i in range(len(star)):
        array = star
        print(array[i])
#------------------------------------------------------------------------------------------
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
    comparelst = [[]]
    randomx = Main.randomnum(20)
    randomy = Main.randomnum(20)
    print("randomx is: "+str(randomx))
    print("randomy is: "+str(randomy))
    comparelst[0].append(randomx)
    comparelst[0].append(randomy)
    for elem in comparelst:
        if elem in output:
            print(elem)
        else:
            print("no mines")
    

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



