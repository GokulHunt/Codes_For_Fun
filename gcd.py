# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 22:14:29 2021

@author: gokul
"""

#Finding gcd using iteration

def gcd_iter(a, b):
    if a > b:
        great = a
    else:
        great = b
    
    for num in range(1, great+1):
        if a%num == 0 and b%num == 0:
            gcd = num
    
    return gcd

gcd_iter(6, 128)


#Finding gcd using recursion based on euclid's algorithm

def gcd_recur(a, b):
    if b==0:
        return a
    else:
        return gcd_recur(b, a%b)

gcd_recur(6, 128)

