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

def mining(a,b,var):
    star[a][b] = '■'
    for i in range(30):
        x = random.randint(0,19)
        y = random.randint(0,20)
        if star[x][y] not in var:
            star[x][y] = '■'
            
    for i in range(len(star)):
        array = star
        print(array[i])


def find(lst):
    new_lst = np.array(lst)
    var = '░'
    indices = np.where(new_lst == var)
    result = list(zip(indices[0],indices[1]))
    output = []
    
    for element in result:
        output.append(list(element))

    checked = difference(output)
    

    comparelst = [[]]
    randomx = random.randint(0,5)
    randomy = random.randint(0,5)
    comparelst[0].append(randomx)
    comparelst[0].append(randomy)

    for elem in comparelst:
        try:
            if elem in output[:-checked]:
                mining(elem[0],elem[1],output)
                print(output)
                print("""
    ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
    ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
    ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝
                """)
                return "gameover"     

            else:
                print("No mines, keep going!")
        except TypeError:
            pass

find.counter = 0

def difference(var):
    find.counter += 1
    check = {}
    for i in range(find.counter):
        check[i] = len(var)
        i += 1
    div1 = list(check.values())
    div2 = list(check.keys())
    try: 
        res = div1[-1]//div2[-1]
        return res
    except ZeroDivisionError:
        pass
    

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