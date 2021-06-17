# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 17:09:46 2021

@author: gokul
"""

n = input("no of points: ")
pts = input() 

collection = [list(p) for p in pts.split(' ')]

def find_if_points_on_line(collection):
    def find_slope(base_point, another_point):
        slope = (int(another_point[1]) - int(base_point[1]))/ (int(another_point[0]) - int(base_point[0]))
        return slope

    first_point = collection[0]
    second_point = collection[1]
    
    actual_slope = find_slope(first_point, second_point)
    
    def y_intercept(point, m):
        x = int(point[0])
        y = int(point[1])
        b = y - (m*x)
        return b
    
    b = y_intercept(first_point, actual_slope)
    line_equation = f"y={actual_slope}*x+{b}"
    
    for i in range(1, len(collection)):
        test_point = collection[i]
        test_slope = find_slope(first_point, test_point)
        if test_slope == actual_slope:
            continue
        else:
            return 0
    return line_equation

print(find_if_points_on_line(collection))
    

    
    