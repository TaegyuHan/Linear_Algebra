def matrix_input(row, col):
    matrix = []
    print(f"숫자 {col}개를 띄어쓰기 하며 입력 해주세요!")
    print("ex)", end="")
    for print_number in range(1, col + 1):
        print(f"{print_number}", end=" ")
    print()
    for number_a in range(row):
        matrix.append(input().split(" "))
    return matrix
