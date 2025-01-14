def matrix_multiplier(matrix_1, matrix_2):
    matrix_1_rows, matrix_1_cols = len(matrix_1), len(matrix_1[0])
    matrix_2_rows, matrix_2_cols = len(matrix_2), len(matrix_2[0])

    # verify if matrix multiplication is possible

    if matrix_1_cols != matrix_2_rows:
        raise ValueError("Invalid matrix dimensions for matrix multiplication.")
    
    matrix_product = [[0 for i in range(matrix_2_cols)] for i in range(matrix_1_rows)]

    for i in range (matrix_1_rows):
        for j in range (matrix_2_cols):
            matrix_product[i][j] = sum(matrix_1[i][k] * matrix_2[k][j] for k in range (matrix_1_cols))
    
    return matrix_product
