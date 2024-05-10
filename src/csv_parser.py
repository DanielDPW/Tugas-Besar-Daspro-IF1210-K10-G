def parse_csv(csv):
    data = []

    with open(csv, 'r') as file:
        row = []
        delimiter = [',',';']
        field = ''
        in_field = False

        for line in file:
            for char in line:
                if char == '"':
                    in_field = not in_field
                elif char in delimiter and not in_field:
                    row.append(field)
                    field = ''
                elif char == '\n' and not in_field:
                    row.append(field)
                    data.append(row)
                    row = []
                    field = ''
                else:
                    field = field + char
            
            if field:
                row.append(field)
                field = ''

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