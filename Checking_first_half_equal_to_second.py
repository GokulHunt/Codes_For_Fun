# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 09:11:21 2021

@author: gokul
"""

def check_lhs_rhs(ip):
    data = []
    for i in ip:
        data.append(int(i))
    
    if len(data)%2 == 1:
        if sum(data[:(len(data))//2]) == sum(data[(len(data)+1)//2 :]):
            print("YES")
        else:
            print("NO")
    else:
        if sum(data[:(len(data))//2]) == sum(data[(len(data))//2 :]):
            print("YES")
        else:
            print("NO")
    
check_lhs_rhs('1222006')
