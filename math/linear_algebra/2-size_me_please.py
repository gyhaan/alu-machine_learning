def matrix_shape(arr):
    """
    Calculates the shape of a matrix (nested list) as a list of integers.

    Args:
        arr (list): A nested list representing the matrix.

    Returns:
        list: The shape of the matrix as a list of integers.
    """
    shape = []

    def check_arr_size(current_arr):
        if isinstance(current_arr, list):
            shape.append(len(current_arr))
            check_arr_size(current_arr[0])

    check_arr_size(arr)
    return shape


# Examples
mat1 = [[1, 2], [3, 4]]
print(matrix_shape(mat1))  # Output: [2, 2]

mat2 = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
print(matrix_shape(mat2))  # Output: [2, 2, 3]

