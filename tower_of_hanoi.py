# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 20:43:29 2021

@author: gokul
"""

#printing each move
def print_move(ring, fr, to):
    print("Move ring "+str(ring)+" from "+str(fr)+" to "+str(to))

#function containing recursive calls to move all the rings from one spike to another
def move_rings(rings, n, fr, to, spare):
    if n == 1:
        if type(rings) == list:
            rings = rings[0]
        print_move(rings, fr, to)
    else:
        move_rings(rings[0:n-1], n-1, fr, spare, to)
        move_rings(rings[-1], 1, fr, to, spare)
        move_rings(rings[0:n-1], n-1, spare, to, fr)

def tower_of_hanoi(rings, n, fr, to, spare):
    move_rings(rings, n, fr, to, spare)
    return "Moved all the rings from "+str(fr)+" to "+str(to)


#function call
print(tower_of_hanoi([1,2,3,4], 4, 'P1', 'P2', 'P3'))