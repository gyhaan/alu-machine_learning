#!/usr/bin/env python3

def add_arrays(arr1, arr2):
    sum = []
    if(len(arr1) != len(arr2)):
        return None
    for i in range(len(arr1)):
        sum.append(arr1[i] + arr2[i])

    return sum

arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]

print(add_arrays(arr1, arr2))
print(arr1)

print(arr2)
print(add_arrays(arr1, [1, 2, 3]))