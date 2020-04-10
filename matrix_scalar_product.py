def matrix_scalar_product(matrix, number):
    # 행렬의 스칼라배
    row_1 = len(matrix)
    col_1 = len(matrix[0])
    scalar_matrix = []
    for row in range(row_1):
        input_list = []
        for col in range(col_1):
            input_list.append(int(number) * int(matrix[row][col]))
        scalar_matrix.append(input_list)
    return scalar_matrix
