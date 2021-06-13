# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 20:43:29 2021

@author: gokul
"""

#printing each move
def print_move(fr, to):
    print("Move from "+str(fr)+" to "+str(to))

#function containing recursive calls to move all the rings from one spike to another
def move_rings(n, fr, to, spare):
    if n == 1:
        print_move(fr, to)
    else:
        move_rings(n-1, fr, spare, to)
        move_rings(1, fr, to, spare)
        move_rings(n-1, spare, to, fr)

#function call
print(move_rings(4, 'P1', 'P2', 'P3'))