from tabulate import tabulate

# QUESTION
"""
Matrix:
[[1, 1, 1]
 [1, 0, 1]
 [1, 1, 1]]

Make all rows and columns zero wherever there is a 0. Make changes in the matrix. You cannot make an entirely new
matrix and then return it.

|1|1|1|             |1|0|1|
|1|0|1|    --->     |0|0|0|
|1|1|1|             |1|0|1|

"""

# BRUTE FORCE METHOD
"""
def markRow(arr, i):
    col = len(arr[0])
    for j in range(col):
        if arr[i][j] != 0:
            arr[i][j] = -1


def markCol(arr, j):
    row = len(arr)
    for i in range(row):
        if arr[i][j] != 0:
            arr[i][j] = -1


def setZeroes(arr):
    row = len(arr)
    col = len(arr[0])

    for i in range(row):
        for j in range(col):
            if arr[i][j] == 0:
                markRow(arr, i)
                markCol(arr, j)

    for i in range(row):
        for j in range(col):
            if arr[i][j] == -1:
                arr[i][j] = 0


arr = [[1, 1, 1, 1],
       [1, 0, 1, 1],
       [1, 1, 0, 1],
       [1, 1, 1, 1]]

setZeroes(arr)

for i in arr:
    print(i)
"""

# BETTER METHOD
"""
def setZeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    row_marker = [0] * rows
    col_marker = [0] * cols

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                row_marker[i] = 1
                col_marker[j] = 1

    for i in range(rows):
        for j in range(cols):
            if row_marker[i] == 1 or col_marker[j] == 1:
                matrix[i][j] = 0
"""


# OPTIMAL SOLUTION
def setZeroes(matrix):
    M, N = len(matrix), len(matrix[0])
    first_row, first_column = False, False

    for c in range(N):
        if matrix[0][c] == 0:
            first_row = True

    for r in range(M):
        if matrix[r][0] == 0:
            first_column = True

    for r in range(1, M):
        for c in range(1, N):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                matrix[r][0] = 0

    for r in range(1, M):
        if matrix[r][0] == 0:
            for c in range(1, N):
                matrix[r][c] = 0

    for c in range(1, N):
        if matrix[0][c] == 0:
            for r in range(1, M):
                matrix[r][c] = 0

    if first_row:
        for c in range(N):
            matrix[0][c] = 0

    if first_column:
        for r in range(M):
            matrix[r][0] = 0

# TABULATE THE MATRIX
"""
def printMatrixSideBySide(matrix1, matrix2):
    formatted_matrix1 = tabulate(matrix1, tablefmt="grid").splitlines()
    formatted_matrix2 = tabulate(matrix2, tablefmt="grid").splitlines()

    height1 = len(formatted_matrix1)
    height2 = len(formatted_matrix2)

    total_height = max(height1, height2)
    arrow_position = total_height // 2

    while len(formatted_matrix1) < total_height:
        formatted_matrix1.append(" " * len(formatted_matrix1[0]))
    while len(formatted_matrix2) < total_height:
        formatted_matrix2.append(" " * len(formatted_matrix2[0]))

    for i in range(total_height):
        line1 = formatted_matrix1[i]
        line2 = formatted_matrix2[i]
        if i == arrow_position:
            print(line1 + "     ----->      " + line2)
        else:
            print(line1 + "                 " + line2)
            
arr = [[1, 1, 1, 1],
       [1, 0, 1, 1],
       [1, 1, 0, 1],
       [1, 1, 1, 1]]

initial_arr = [row[:] for row in arr]

setZeroes(arr)

printMatrixSideBySide(initial_arr, arr)
"""

arr = [[1, 1, 1, 1],
       [1, 0, 1, 1],
       [1, 1, 0, 1],
       [1, 1, 1, 1]]

setZeroes(arr)
print(arr)
