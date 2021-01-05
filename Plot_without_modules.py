# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 16:20:17 2020

@author: Gokul
"""

n = int(input("Enter the no of elements: "))
l = [int(input()) for i in range(n)]

#Sample Input: 
#l =  [3, 1, 2, 4, 5]
#l = [1, 3, 3, 4, 5, 2, 1, 2, 3, 1, 2, 6, 2, 3, 6, 2, 3, 6, 3, 2, 3, 1, 5, 3, 2, 1, 2, 4 , 2, 1, 8, 1, 2]

row = sum(l)
col = sum(l)
 
# Empty list called matrix
matrix = []


#initializing an empty matrix
for i in range(2*row):
    a =[]
    for j in range(2*col):
         a.append(' ')
    matrix.append(a)

 
#Plotting the numbers into the matrix
ro = int(len(matrix)/2 - 1)
co = 0

for ele in range(0, len(l)):
    if int(ele)%2 == 0:
        for val in range (0, l[ele]):
            matrix[ro-val][co+val] = '/'
        ro = ro-val
        co = co+val+1
    else:
        for val in range(0, l[ele]):
            matrix[ro+val][co+val] = '\\'
        ro = ro+val
        co = co+val+1


#To get the column having the Peak
for i in range(2*row):
    flag = False
    for j in range(col):
        if matrix[i][j] == '/':
            row_new = i
            col_new = j
            print(col_new)
            flag = True
            break
    if flag == True:
        break


#Inserting a balnk space next to the peak for inserting the figure    
for lst in range(len(matrix)):
    matrix[lst].insert(col_new+1, ' ')


#Inserting the figure around the peak
for i in range(2*row):
    flag = False
    for j in range(col):
        if matrix[i][j] == '/':
            matrix[i-1][j] ='<'
            matrix[i-1][j+2]='>'
            matrix[i-2][j]='/'
            matrix[i-2][j+1]='|'
            matrix[i-2][j+2]='\\'
            matrix[i-3][j+1]='o'
            flag = True
            break
    if flag == True:
        break


#Printing the plot from the matrix
for i in range(2*row):
    for j in range(2*col):
        print(matrix[i][j], end = ' ')
    print()