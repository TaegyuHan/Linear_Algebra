from fractions import Fraction
from matrix_elementary_column_operation import *
from matrix_make_inverse import *
from matrix_minus import *
from matrix_multiplication import *
from matrix_plus import *
from matrix_scalar_product import *
from matrix_show import *

a = [[1, 3, 3, 8], [-2, -5, 1, -8], [0, 1, 7, 8]]
i = [[1, 0, 0, 0], [0, 1, 0], [0, 0, 1]]
a1 = [[1, 0], [-2, 3]]

matrix_show(a1)
a = matrix_elementray_scalar_plus(a1, 1, 2, 2)
matrix_show(a1)
a = matrix_elementray_scalar_product(a1, 2, Fraction(1, 3))
matrix_show(a1)
matrix_show(a1)
