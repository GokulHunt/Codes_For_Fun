# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 20:48:34 2021

@author: gokul
"""


def print_matrix(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            print(matrix[row][column], end = '  ')
        print("")
        
def matrix_multiplication(A, B):
    C = []
    
    for i in range(len(A)):
        temp = []
        for j in range(len(B)):
            temp.append(0)
        C.append(temp)
        
    for i in range(0, len(A)):
        for j in range(0, len(B[0])): 
            out = 0
            for k in range(0, len(B)):
                out += A[i][k]*B[k][j]
            C[i][j] = out

    return C

A = [[1, 2],
     [3, 4]]

B = [[1, 2],
     [0, 1]]

output = matrix_multiplication(A, B)
print_matrix(output)
