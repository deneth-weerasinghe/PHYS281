import math

A = [[2, 1], [4, 8], [7, 5]]
B = [[4, 6], [2, 7]]


def matrixmult(A, B):

    '''
    :param A: 2D nested list; the matrix that is the multiplier
    :param B: 2D nested list; the matrix that is the multiplicand
    :return: 2D nested list; product of the matrix multiplication

    --------------------------------------------------------------
    function calculates the matrix product of the to matrix arguments
    and raises errors if appropriate

    '''

    if len(A[0]) != len(B):
        raise ValueError("Cannot multiply the two matrices A and B. Number of columns in A is not equal to the number of rows in B")
    for i in A:
        if len(i) != len(A[0]):
            raise ValueError("Matrix A is invalid, number of columns in a row is not consistent")
    for i in B:
        if len(i) != len(B[0]):
            raise ValueError("Matrix B is invalid, number of columns in a row is not consistent")

    product_matrix = []
    for i in range(0, len(A)):
        row_element = []
        for j in range(0, len(B[0])):
            element_sum = 0
            for k in range(0, len(B)):
                element_sum += A[i][k] * B[k][j]
            row_element.append(element_sum)
        product_matrix.append(row_element)
    return product_matrix

x = math.pi / 2
A = [[math.cos(x), -math.sin(x)], [math.sin(x), math.cos(x)]]
B = [[1], [0, 0]]
try:
    C = matrixmult(A, B)
except ValueError as inst:
    print("Caught ValueError")
    print("You have thrown the right type of error")

