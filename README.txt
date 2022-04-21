

How to create a minesweeper-like game using python3.8.0

Medium link = https://medium.com/@francisco.mauratay/python-minesweeper-9ea4713f717

I started with the naive assumption that a minesweeper would be something easy to build, even though the result is simple, it wasn’t that easy to code :’)

I couldn’t come up with a circule-ish pattern like the original minesweeper:



Nonetheless I was able to come up with something similar that covers few angles when it comes to discovering the mines.
First part is a class that covers the blueprint and a verifier, the verifier makes sure that the input number is not bigger than 20 nor smaller than 0, the blueprint is  the lists full of ‘M’s.



After the blueprint there are the rules for the field that’ll be revealed:

Here it covers the multidimensional arrays to reveal with '░'.
Makes sure the ‘x’s are not bigger/smaller than 19/0 and the ‘y’s not bigger/smaller than 20/0, by checking the combination of the coordinate x/y with a random number, and sets that by assigning it to the multidimensional array star >  star[x][y]

That makes the effect of revealing '░' by printing that out to the terminal:
e.g.


The background is:

Which assigns the value of '■' to the multidimensional array with the user input (x,y)
And then prints out the whole multidimensional array.

To set the mines:


First make sure that the mine is not assigned to an already revealed coordinate, then assign the coordinate to the new mines and print out the blueprint.

And here comes a bit of mixing, finding the revealed items in the lists, assigning random mines, and finding out if the input coordinates landed on a mine:


First get a count of the revealed items and append them to an ingeniously named list: “revealed”.
Create 30 mines and spread them randomly throughout the lists, if one of them is in revealed, is game over, if you want to make it easier, just go ahead and lower that range down as you please.

Put it all together and keep on running until you get a “game over”:








