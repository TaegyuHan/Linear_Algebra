def matrix_multiplication(matrix_1, matrix_2):
    #  행렬의 곱
    row_1 = len(matrix_1)
    col_1 = len(matrix_1[0])
    row_2 = len(matrix_2)
    col_2 = len(matrix_2[0])
    multip_matrix = []
    if col_1 == row_2:
        for num in range(row_1):  # 2
            input_list = []
            for row_list_num in range(col_2):  # 2
                sum_list = []
                for row_num in range(row_2):  # 3
                    sum_list.append(
                        matrix_1[num][row_num] * matrix_2[row_num][row_list_num]
                    )
                input_list.append(sum(sum_list))
            multip_matrix.append(input_list)
        return multip_matrix
    else:
        print("행렬의 곱을 할 수 없습니다.")
