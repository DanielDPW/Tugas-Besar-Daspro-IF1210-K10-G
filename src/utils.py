import sys
import os

from typing import *
from .types import *

def split(x: str, delimiter: str) -> Array:
    lst = []
    string = ""
    for i in range(len(x)):
        if x[i] != delimiter:
            string = string + x[i]
        else:
            lst.append(string)
            string = ""
    lst.append(string)
    return lst

def remove_x_line_above(x : int):
    for i in range(x):
        sys.stdout.write("\033[F")
        sys.stdout.write("\033[K")
        sys.stdout.flush()

def remove_xth_line_above(x : int):
    for i in range(x):
        sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    sys.stdout.flush()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def max(a: int, b: int) -> int:
    if a >= b:
        return a
    return b

def min(a: int, b: int) -> int:
    if a <= b:
        return a
    return b

def title(s : str) -> str:
    capitalize = True
    new_string = ''
    for char in s:
        if capitalize:
            new_string = new_string + char.upper()
            capitalize = False
        else:
            new_string = new_string + char
        if char == ' ':
            capitalize = True
    return new_string

def is_int(string : str) -> bool:
    int_char = ['0','1','2','3','4','5','6','7','8','9']
    for char in string:
        if char not in int_char:
            return False
    return True

def is_in_column(matrix : Matrix, index : int, x : str) -> bool:
    for row in matrix:
        if x == row[index]:
            return True
    return False

def is_empty(array : Array) -> bool:
    if len(array) == 0:
        return True
    for element in array:
            if element:
                return False
    return True

def copy_array(array : Array) -> Array:
    new_array = []
    
    for i in range(len(array)):
        new_array.append(array[i])
    
    return new_array

def remove_value(array : Array, value : str) -> Array:
    return [item for item in array if item != value]

def remove_row(matrix : Matrix, index : Optional[int] = None, element : Optional[str] = None) -> Matrix:
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

def slice_matrix(matrix : Matrix, row_start : Optional[int] = None, row_stop : Optional[int] = None, row_step : Optional[int] = None, col_start : Optional[int] = None, col_stop : Optional[int] = None, col_step : Optional[int] = None) -> Matrix:
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

def is_space(x : str) -> bool:
    whitespace_chars = [' ', '\t', '\n', '\r', '\f', '\v']
    if len(x) == 0:
        return True
    else:
        for char in x:
            if char not in whitespace_chars:
                return False
        return True

def is_in_dict(dict_list : DictList, key : str, value : str) -> bool:
    for dictionary in dict_list:
        if key in dictionary and dictionary[key] == value:
            return True
    return False

def find_row(matrix : Matrix, index : int, element : str) -> int:
    for i, row in enumerate(matrix):
        if index <= len(row) and row[index] == element:
            return i
    return -1

def find_dict_index(dict_list : DictList, key: str, value: str) -> int:
    for i, dictionary in enumerate(dict_list):
        if key in dictionary and dictionary[key] == value:
            return i
    return -1

def ascending_sort(array : Array) -> Array:
    n = len(array)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]
    
    return array

def strip(line: str) -> str:
    new_line = ""
    x = 0
    y = len(line) - 1
    while x < len(line) and is_space(line[x]):
        x = x + 1
    while y >= x and is_space(line[y]):
        y = y - 1

    for i in range(x, y + 1):
        new_line = new_line + line[i]

    return new_line