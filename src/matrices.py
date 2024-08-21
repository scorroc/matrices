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
            row.append(float("{:.2f}".format(matrix1[i][j]*num)))
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

def matrix_determinant(matrix):
    newMatrix = matrix
    determinant = 0

    #Si la matriz es de 2x2, no tenemos que agregar filas, por lo que calculamos directamente la determinante
    if((2,2) == get_matrix_size(matrix)):
        return matrix[0][0]*matrix[1][1] - (matrix[1][0]*matrix[0][1])


    #Agregamos las primeras filas al final, para poder obtener las diagonales necesarias para calcular el determinante
    for i in range(len(matrix)-1):
        newMatrix.append(matrix[i])
    
    #Calculamos la suma de los productos de las diagonales que van hacia la derecha
    for i in range(len(matrix[0])):
        result = 1
        for j in range(len(matrix[0])):
            result = result*newMatrix[i][j]
            i = i+1
        determinant = determinant + result

    #Calculamos la suma de los productos de las diagonales que van hacia la izquierda
    for i in range(len(matrix[0])):
        result = 1
        #Recorremos la fila de manera inversa, para poder encontrar la diagonal empezando por la derecha
        for j in range(len(matrix[0])-1, -1, -1):
            result = result*newMatrix[i][j]
            i = i+1
        determinant = determinant - result

    return determinant

def delete_position(matrix,row,column):
    newMatrix = []
    for i in range(len(matrix[0])):
        newRow = []
        for j in range(len(matrix)):
            if( i != row):
                if(j!=column):
                    newRow.append(matrix[i][j])
        if(newRow != []):
            newMatrix.append(newRow)

    return newMatrix

def adjugate_matrix(matrix):
    sign = 1
    adjugateMatrix = []
    for i in range(len(matrix)):
        newRow = []
        for j in range(len(matrix)):
            auxMatrix = delete_position(matrix,i,j)
            newRow.append(sign*matrix_determinant(auxMatrix))
            sign = sign*-1
        adjugateMatrix.append(newRow)
    return adjugateMatrix

def inverse_matrix(matrix):
    adjugate = adjugate_matrix(matrix)

    determinant = matrix_determinant(matrix)

    adjugateTransposed = transpose_matrix(adjugate)

    inverse = scalar_multiplication(adjugateTransposed,1/determinant)

    return inverse

matriz = create_matrix(3,3,[3,4,-1,2,0,1,1,3,-2])
matriz2 = create_matrix(3,3,[-3,2,0,1,-1,2,-2,1,3])

inverse = inverse_matrix(matriz)

print("Inverse matrix = ")
print_matrix(inverse)