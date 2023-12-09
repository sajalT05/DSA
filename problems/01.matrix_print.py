'''
traverse though nXn matrix with O(n) time complexity
'''

MATRIX = [[1,2,3],[5,6,7],[8,9,10]]

def traverse_matrix(matrix: list) -> int:
    '''
    INPUT: matrix (NXN) -> (list)

    PROCESS:
        - check input type is list
        - find rows, columns, and total elements
        - traverse through every index, find row-id & column-id.
    '''
    if isinstance(matrix,list):
        pass
    else:
        return "input type is not list"

    row = len(matrix) # total rows
    column = len(matrix[0]) # total columns
    elements = row * column

    temp = 0

    for element in range(0,elements):
        row_id = element//column
        column_id = element-row_id*column
        temp = matrix[row_id][column_id]
        print(temp)


traverse_matrix(matrix=MATRIX)
