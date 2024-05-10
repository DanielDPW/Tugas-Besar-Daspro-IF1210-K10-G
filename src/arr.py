def is_in_column(matrix, index : int, x : str) -> bool:
    for row in matrix:
        if x == row[index]:
            return True
    return False

def is_in_row(matrix, index : int, x : str) -> bool:
    if x in matrix[index]:
        return True
    else:
        return False

def is_empty(array) -> bool:
    return len(array) == 0

def row_length(matrix) -> int:
    if matrix:
        return len(matrix[0])
    else:
        return 0

def column_length(matrix) -> int:
    if matrix:
        return len(matrix)
    else:
        return 0

def remove_empty_row(matrix):
    new_matrix = []

    for row in matrix:
        if any(row):
            new_matrix.append(row)

    return new_matrix

def copy_matrix(matrix):
    new_matrix = [[None] * len(matrix[0]) for i in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix [i][j] = matrix[i][j]

    return new_matrix

def copy_array(array):
    new_array = []
    
    for i in range(len(array)):
        new_array.append(array[i])
    
    return new_array

def remove_row(matrix, index = None, element = None):
    new_matrix = []
    
    if index is not None and element is None:
        for i, row in enumerate(matrix):
            if i != index:
                new_matrix.append(row)
    elif element is not None and index is None:
        for row in matrix:
            if element not in row:
                new_matrix.append(row)
    elif element is not None and index is not None:
        for row in matrix:
            if index >= len(row) or row[index] != element:
                new_matrix.append(row)
    else:
        new_matrix = matrix

    return new_matrix

def copy_row(matrix, index = None, element = None):
    new_matrix = []
    
    if index is not None and element is None:
        for i, row in enumerate(matrix):
            if i == index:
                new_matrix.append(row)
    elif element is not None and index is None:
        for row in matrix:
            if element in row:
                new_matrix.append(row)
    elif element is not None and index is not None:
        for row in matrix:
            if index <= len(row) and row[index] == element:
                new_matrix.append(row)
    else:
        new_matrix = matrix

    return new_matrix

def slice_array(array, start = None, stop = None, step = None):
    if start is None:
        start = 0
    if stop is None:
        stop = len(array)
    if step is None:
        step = 1

    new_array = []
    for i in range(start, stop, step):
        new_array.append(array[i])

    return new_array

def slice_matrix(matrix, row_start = None, row_stop = None, row_step = None, col_start = None, col_stop = None, col_step = None):
    if row_start is None:
        row_start = 0
    if row_stop is None:
        row_stop = len(matrix)
    if col_start is None:
        col_start = 0
    if col_stop is None:
        col_stop = len(matrix[0])
    if row_step is None:
        row_step = 1
    if col_step is None:
        col_step = 1

    new_matrix = []
    for i in range(row_start, row_stop, row_step):
        temp_row = []
        for j in range(col_start, col_stop, col_step):
            temp_row.append(matrix[i][j])
        new_matrix.append(temp_row)

    return new_matrix

def is_space(x):
    whitespace_chars = [' ', '\t', '\n', '\r', '\f', '\v']
    if len(x) == 0:
        return True
    else:
        for char in x:
            if char not in whitespace_chars:
                return False
        return True

def find_row(matrix, index : int, element : str) -> int:
    for i, row in enumerate(matrix):
        if index <= len(row) and row[index] == element:
            return i
    return -1

def strip(x: str) -> str:
    new_string = ''
    whitespace_chars = [' ', '\t', '\n', '\r', '\f', '\v']
    
    for char in x:
        if char not in whitespace_chars:
            new_string = new_string + char
    return new_string