def create_matrix(rowNum, columnNum, data):
    matrix = []
    for i in range(rowNum):
        row = []
        for j in range(columnNum):
            row.append(data.pop(0))
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

matriz = create_matrix(3,3,[1,2,3,4,5,6,7,8,9])

print_matrix(matriz)