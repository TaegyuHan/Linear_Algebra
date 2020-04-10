def matrix_show(matrix):
    # 행렬보여주기
    print("행렬")
    for row in matrix:
        for row_number in row:
            print(row_number, end="\t")
        print()
