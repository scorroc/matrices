def create_matrix(rowNum, columnNum, data):
    matrix = []
    for i in range(rowNum):
        row = []
        for j in range(columnNum):
            row.append(data.pop(0))
        matrix.append(row)
    return matrix

def create_zero_matrix(rowNum, columnNum):
    matrix = []
    for i in range(rowNum):
        row = []
        for j in range(columnNum):
            row.append(0)
        matrix.append(row)
    return matrix

def create_diagonal_matrix(data):
    diagonalMatrix = []

    for i in range(len(data)):
        row = []
        for j in range(len(data)):
            if i == j:
                row.append(data[i])
            else:
                row.append(0)
        diagonalMatrix.append(row)
    return diagonalMatrix

def create_identity_matrix(size):
    identityMatrix = []
    for i in range(size):
        row = []
        for j in range(size):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        identityMatrix.append(row)
    return identityMatrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

def get_position(matrix,rowPos, colPos):
    return matrix[rowPos-1][colPos-1]

def get_column(matrix,col):
    column = []
    for i in range(len(matrix)):
        column.append(matrix[i][col-1])
    return column

def get_row(matrix,row):
    return matrix[row-1]

def get_main_diagonal(matrix):
    mainDiagonal = []
    for i in range(len(matrix)):
        mainDiagonal.append(matrix[i][i])
    return mainDiagonal

def get_matrix_size(matrix):
    return (len(matrix),len(matrix[0]))

def equals(matrix1, matrix2):
    if matrix1 == matrix2:
        return True
    else: 
        return False

def transpose_matrix(matrix):
    size = get_matrix_size(matrix)
    colNum = size[1]
    transposed = []
    i = 0

    for j in range(colNum):
        newRow = []
        for row in matrix:   
            newRow.append(row[i])
        transposed.append(newRow)
        i = i+1

    return transposed
    
def matrix_sum(matrix1, matrix2): 
    size = get_matrix_size(matrix1)
    rowNum = size[0]
    colNum = size[1]

    result = []

    for i in range(rowNum):
        row = []
        for j in range(colNum):
            row.append(matrix1[i][j]+matrix2[i][j])
        result.append(row)
    
    return result

def scalar_multiplication(matrix1,num):
    size = get_matrix_size(matrix1)
    rowNum = size[0]
    colNum = size[1]

    result = []

    for i in range(rowNum):
        row = []
        for j in range(colNum):
            row.append(matrix1[i][j]*num)
        result.append(row)
    return result

def matrix_multiplication(matrix1, matrix2):
    resultMatrix = []
    for mat1Row in matrix1:
        i = 0
        newRow = []
        for x in range (len(matrix1)):
            j = 0
            result = 0
            for mat2Row in matrix2:
                result = result + mat1Row[j]*mat2Row[i]
                j = j+1
            i = i+1  
            newRow.append(result)
        resultMatrix.append(newRow)
        
    return resultMatrix

matriz = create_matrix(3,3,[1,2,3,4,5,6,7,8,9])

matriz1 = create_matrix(2,3,[4,3,2,1,2,3])

matriz2 = create_matrix(3,2,[0,1,1,2,-1,0])

print("Matriz 1")
print_matrix(matriz1)

print("Matriz2")
print_matrix(matriz2)

print("Resultado")
res = matrix_multiplication(matriz2,matriz1)
print_matrix(res)