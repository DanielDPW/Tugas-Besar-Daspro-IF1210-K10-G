from . import utils

def parse_csv(csv):
    with open(csv, 'r') as file:
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
                    print("Some data is missing or exceeds the header columns!")
                    return None
                data.append(row)
    return data

def generate_csv(matrix, csv):
    with open(csv, 'w') as file:

        for row in matrix:
            line = ''

            for i, field in enumerate(row):
                line = line + str(field)
                if i < len(row) - 1:
                    line = line + ';'

            file.write(line + '\n')