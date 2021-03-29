#sudoku
#fill_in_box not yet

import numpy as np

def find_empty(matrix):
    for i in range(9):
        prod = int(1)
        for j in range(9):
            prod = int(prod*matrix[i][j])
        if prod == 0:
            return i+1 # return empty row, 1-9
    return 0 # sudoku completed

def fill_in_row(matrix):
    for i in range(9):
        arr = [x+1 for x in range(9)]
        for j in range(9):
            if matrix[i][j] != 0:
                arr.remove(matrix[i][j])
            else:
                key = j
        if len(arr)==1:
            matrix[i][key]=arr[0]
    
def fill_in_col(matrix):
    for j in range(9):
        arr = [x+1 for x in range(9)]
        for i in range(9):
            if matrix[i][j] != 0:
                arr.remove(matrix[i][j])
            else:
                key = i
        if len(arr)==1:
            matrix[key][j]=arr[0]

def fill_in_box(matrix):
    # 1 2 3
    # 4 5 6
    # 7 8 9
    mat[0]=matrix[0:2,]
    mat[1]=matrix[3:5,]
    mat[2]=matrix[6:8,]
    for i in range(3):
        mat[i][0]=mat[i,0:2]
        mat[i][1]=mat[i,3:5]
        mat[i][2]=mat[i,6:8]
    
    for i in range(3):
        for j in range(3):
            mat = sum(mat[i][j],[])
            arr = [x+1 for x in range(9)]
            for k in range(9):
                if mat[k] != 0:
                    arr.remove(mat[k])
                else:
                    key = k
            if len(arr)==1:
                matrix[k]=arr[0]
            matrix[mat_arr[i]][mat_arr[j]] = [list(map(int, mat)) for i in range(9)]
            

matrix = [list(map(int, input().split())) for i in range(9)]

while find_empty(matrix) != 0:
    fill_in_row(matrix)
    fill_in_col(matrix)
    fill_in_box(matrix)

print(matrix)