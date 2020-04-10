from matrix_elementary_column_operation import matrix_elementray_scalar_product
from matrix_show import matrix_show


def matrix_make_inverse(matrix):
    matrix = matrix
    matrix_row_int = len(matrix)
    matrix_col_int = len(matrix[0])
    for num_col in []:
        if matrix[0][0] != 1:
            matrix = matrix_elementray_scalar_product(matrix, 1, 1 / matrix[0][0])

    return matrix
