from . import utils
from typing import *

from .types import *

def parse_csv(csv : str) -> Matrix:
    with open(csv, 'r') as file:

        # Inisialisasi headers
        headers = []
        found_headers = False
        
        for line in file:
            if not found_headers:
                headers = utils.split(utils.strip(line), ';')
                found_headers = True
                data = [headers]
            else:
                row = utils.split(utils.strip(line), ';')
                if len(row) != len(headers):
                    print("File tidak dapat diproses lebih lanjut karena tidak sesuai dengan header!")
                    return None
                data.append(row)
    return data

def generate_csv(matrix : Matrix, csv : str):
    with open(csv, 'w') as file:

        for row in matrix:
            line = ''

            for i, field in enumerate(row):
                line = line + str(field)
                if i < len(row) - 1:
                    line = line + ';'

            file.write(line + '\n')