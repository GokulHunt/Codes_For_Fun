# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 15:46:29 2021

@author: gokul
"""

#using normal recursion
def fibonacci_rec(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)

# Function for nth fibonacci 
# number - Dynamic Programing
# Taking 1st two fibonacci nubers as 0 and 1

FibArray = [0, 1]
def fibonacci_dynp(n):
   
    # Check is n is less 
    # than 0
    if n < 0:
        print("Incorrect input")
         
    # Check is n is less 
    # than len(FibArray)
    elif n < len(FibArray):
        return FibArray[n]
    else:
        temp_fib = fibonacci_dynp(n - 1) + fibonacci_dynp(n - 2)
        FibArray.append(temp_fib)
        return temp_fib
 
# Driver Program
print(fibonacci_dynp(9))

def fibonacci_iter(n):
    a = 0
    b = 1
    
    # Check is n is less
    # than 0
    if n < 0:
        print("Incorrect input")
         
    # Check is n is equal
    # to 0
    elif n == 0:
        return 0
       
    # Check if n is equal to 1
    elif n == 1:
        return b
    else:
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
            
        return b


#dynamic programming using dictionary    
def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans
    
d = {0:0, 1:1, 2:1}
print(fib_efficient(9, d))