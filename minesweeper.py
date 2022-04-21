#!/usr/bin/env python3

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

# --------------------------------------

star = Main.blueprint

def surround(y,x):
    ran = random.randint(0,10)
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

def mining(lst,lst2):
    for item in lst:
        if item not in lst2:
            star[item[0]][item[1]] = '■'
            
    for i in range(len(star)):
        array = star
        print(array[i])


def find(lst):
    new_lst = np.array(lst)
    var = '░' 
    indices = np.where(new_lst == var)
    result = list(zip(indices[0],indices[1]))
    revealed = []
    
    for element in result:
        revealed.append(list(element))
    
    mine_list = []

    for i in range(20):
        x = random.randint(0,19)
        y = random.randint(0,20)
        doubles = []
        doubles.append(x)
        doubles.append(y)
        mine_list.append(doubles)
        i += 1
        
    for elem in mine_list:
        
        if elem in revealed:
            mining(mine_list,revealed)
            print("""
    ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
    ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
    ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
                """)
            return "gameover"     


    

def shot():
    y = input("Select by coordinate Y: (from 19 to 0)\n")
    y = Main.verifier(y)
    x = input("Select by coordinate X: (from 20 to 0)\n")
    x = Main.verifier(x)
    background(y,x)
    if find(star) == "gameover":
        return "gameover"
  

while shot() != "gameover":
    if shot() == "gameover":
        break