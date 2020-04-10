def matrix_plus(matrix_1, matrix_2):
    # 행렬의 덧셈
    row_1 = len(matrix_1)
    col_1 = len(matrix_1[0])
    row_2 = len(matrix_2)
    col_2 = len(matrix_2[0])
    plus_matrix = []
    if row_1 == row_2 and col_1 == col_2:
        for row in range(row_1):
            input_list = []
            for col in range(col_1):
                input_list.append(int(matrix_1[row][col]) + int(matrix_2[row][col]))
            plus_matrix.append(input_list)
    else:
        print(" 행과 열이 같지 않아 더할 수 없습니다.")
    return plus_matrix
