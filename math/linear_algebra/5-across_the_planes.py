#!/usr/bin/env python3

""""
This is module for 
adding matrices
"""


def check_shape(arr):
    shape_arr = []

    while(isinstance(arr,list)):
        shape_arr.append(len(arr))
        arr = arr[0]
    
    return shape_arr

def add_matrices2D(mat1, mat2):

    """"
    This is for addition
    """


    sum = []

    if(check_shape(mat1) != check_shape(mat2)):
        return None
    
    for i in range(len(mat1)):
        sum_row = []
        for j in range(len(mat1)):
            sum_row.append(mat1[i][j] + mat2[i][j])
        
        sum.append(sum_row)

    print(sum)
    return sum