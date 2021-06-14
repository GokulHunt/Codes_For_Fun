# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 22:07:39 2021

@author: gokul
"""

#determining whether a value is int
def isint(val):
    try:
        if type(int(val)) ==  int:
            return True
    except:
        return False

ip = '123jbsjbs78hsbjz097744msk'
sum = 0

#printing the letters and adding up the integers and printing their sum
i=0
while i>= 0 and i<len(ip):
    if ip[i] in 'abcdefghijklmnopqrstuvwxyz':
        print(ip[i])
        i+=1
    else:
        num = ''
        while isint(ip[i]) == True:
            num+=ip[i]
            i+=1
        sum += int(num)
        
print(sum)
