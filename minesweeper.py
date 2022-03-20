#!/usr/bin/env python3

"""
Deadline:
Friday

Pseudo Code

1 make square 25 x 25 asterisc long
2 each asterisc is a random number     
3 limit random number from 1 to 10
4 each try the random number is reduced by 2 until reaching one and then back to 10
5 the asteriscs around the one picked are to be taken out
6 random asteriscs are mines, if one's hit, game over
"""

import random


class Asterisc:

    blueprint = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(19):
        new = blueprint
        new[i].append('*')
        for i in range(19):
            new = blueprint
            new[i].append('*')
        

    def reset(self):
        for i in range(19):
            new = self.blueprint
            new[i].append('*')
            for i in range(19):
                new = self.blueprint
                new[i].append('*')
        return self.blueprint

    def random_number(x):
        result = random.randrange(0,x,2)
        return result
# --------------------------------------

def background(y,x):
    star = Asterisc.blueprint
    y = int(y)
    x = int(x)
    star[y][x]= 'X'
    print("""
███╗░░░███╗██╗███╗░░██╗███████╗░██████╗░██╗░░░░░░░██╗███████╗███████╗██████╗░███████╗██████╗░
████╗░████║██║████╗░██║██╔════╝██╔════╝░██║░░██╗░░██║██╔════╝██╔════╝██╔══██╗██╔════╝██╔══██╗
██╔████╔██║██║██╔██╗██║█████╗░░╚█████╗░░╚██╗████╗██╔╝█████╗░░█████╗░░██████╔╝█████╗░░██████╔╝
██║╚██╔╝██║██║██║╚████║██╔══╝░░░╚═══██╗░░████╔═████║░██╔══╝░░██╔══╝░░██╔═══╝░██╔══╝░░██╔══██╗
██║░╚═╝░██║██║██║░╚███║███████╗██████╔╝░░╚██╔╝░╚██╔╝░███████╗███████╗██║░░░░░███████╗██║░░██║
╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝╚═════╝░░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝
    """)
    for i in range(len(star)-1):
        array = star
        print(array[i])
    print("""
╭━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━╮
╰━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━╯
    """)


def verifier(num):
    num = int(num)
    if num > 20:
        raise Exception("Error number should be smaller than 19")
    elif num < 0:
        raise Exception("Error number should be bigger than 0")
    else:
        return num

def shot():
    y = input("Select by coordinate Y: (from 0 to 19)\n")
    y = verifier(y)
    x = input("Select by coordinate X: (from 0 to 19)\n")
    x = verifier(x)
    background(y,x)

again = True

shot()

while again == True:
    ans = input("Another one? [y] [n]\n")
    if ans == 'y':
        shot()
    elif ans == 'n':
        print("Goodbye!")
        break





