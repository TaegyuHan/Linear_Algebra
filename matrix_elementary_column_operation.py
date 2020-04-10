def matrix_elementray_exchange(matrix, row_num_1, row_num_2):
    matrix = matrix
    row_list_indexing_num_1 = int(row_num_1) - 1
    row_list_indexing_num_2 = int(row_num_2) - 1
    matrix_list_number_1 = matrix[row_list_indexing_num_1]
    matrix_list_number_2 = matrix[row_list_indexing_num_2]
    matrix[row_list_indexing_num_1] = matrix_list_number_2
    matrix[row_list_indexing_num_2] = matrix_list_number_1
    return matrix


def matrix_elementray_scalar_product(matrix, row_num, scalar_number):
    matrix = matrix
    row_num = int(row_num) - 1
    scalar_number = scalar_number
    scalar_number_list = []
    for num in range(len(matrix[0])):
        scalar_number_list.append(scalar_number * matrix[row_num][num])
    matrix[row_num] = scalar_number_list
    return matrix


def matrix_elementray_scalar_plus(matrix, row_num_1, row_num_2, scalar_number):
    matrix = matrix
    row_list_indexing_num_1 = int(row_num_1) - 1
    row_list_indexing_num_2 = int(row_num_2) - 1
    scalar_number = scalar_number
    scalar_number_list_1 = []
    scalar_number_list_2 = []
    for num in range(len(matrix[0])):
        scalar_number_list_1.append(
            scalar_number * matrix[row_list_indexing_num_1][num]
        )
    for num in range(len(matrix[0])):
        scalar_number_list_2.append(
            matrix[row_list_indexing_num_2][num] + scalar_number_list_1[num]
        )
    matrix[row_list_indexing_num_2] = scalar_number_list_2
    return matrix
