# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 22:35:16 2021

@author: gokul
"""

def genSubsets(L):
    if len(L) == 0:
        return [[]]
    smaller = genSubsets(L[:-1])
    extra = L[-1:]
    new = []
    for small in smaller:
        new.append(small+extra)
    return smaller+new


s = genSubsets([1, 2, 3, 4, 5])