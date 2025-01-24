#!/usr/bin/env python3

def matrix_shape(arr):
    arr1 = [len(arr)]
    def check_arr_size(arr2):
        if(isinstance(arr2, list)):
            arr1.append(len(arr2))
            check_arr_size(arr2[0])
    
    check_arr_size(arr[0])
    return arr1

mat1 = [[1, 2], [3, 4]]
print(matrix_shape(mat1))

mat2 = [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],
        [[16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]]
print(matrix_shape(mat2))